# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import

_package_data = dict(
    full_package_name='string_formatter',
    version_info=(1, 1, 0),
    __version__='1.1.0',
    author='Anthon van der Neut',
    author_email='a.van.der.neut@ruamel.eu',
    description='replacement for string.Formatter, supporting empty keys (recursively)',
    entry_points=None,
    since="2015",
    license='MIT license',
    status="stable",
    universal=1,
    install_requires=dict(),
    tox=dict(env="*"),
)


version_info = _package_data['version_info']
__version__ = _package_data['__version__']

import sys # NOQA
from string import *  # NOQA
import string # NOQA


class Formatter(string.Formatter):
    # if sys.version_info < (3, 5):
    #     def format(self, format_string, *args, **kwargs):
    #         return self.vformat(format_string, args, kwargs)

    def vformat(self, format_string, args, kwargs):
        used_args = set()
        result, _ = self._vformat(format_string, args, kwargs, used_args, 2)
        self.check_unused_args(used_args, args, kwargs)
        return result

    def _vformat(
        self, format_string, args, kwargs, used_args, recursion_depth, auto_arg_index=0
    ):
        if recursion_depth < 0:
            raise ValueError('Max string recursion exceeded')
        result = []
        for literal_text, field_name, format_spec, conversion in self.parse(format_string):

            # output the literal text
            if literal_text:
                result.append(literal_text)

            # if there's a field, output it
            if field_name is not None:
                # this is some markup, find the object and do
                #  the formatting

                # handle arg indexing when empty field_names are given.
                if field_name == '':
                    if auto_arg_index is False:
                        raise ValueError(
                            'cannot switch from manual field specification to '
                            'automatic field numbering'
                        )
                    field_name = str(auto_arg_index)
                    auto_arg_index += 1
                elif field_name.isdigit():
                    if auto_arg_index:
                        raise ValueError(
                            'cannot switch from manual field specification to '
                            'automatic field numbering'
                        )
                    # disable auto arg incrementing, if it gets
                    # used later on, then an exception will be raised
                    auto_arg_index = False

                # given the field_name, find the object it references
                #  and the argument it came from
                obj, arg_used = self.get_field(field_name, args, kwargs)
                used_args.add(arg_used)

                # do any conversion on the resulting object
                obj = self.convert_field(obj, conversion)

                # expand the format spec, if needed
                format_spec, auto_arg_index = self._vformat(
                    format_spec,
                    args,
                    kwargs,
                    used_args,
                    recursion_depth - 1,
                    auto_arg_index=auto_arg_index,
                )

                # format the object and append to the result
                result.append(self.format_field(obj, format_spec))

        return ''.join(result), auto_arg_index

    def convert_field(self, value, conversion):
        # do any conversion on the resulting object
        if conversion is None:
            return value
        elif conversion == 's':
            return str(value)
        elif conversion == 'r':
            return repr(value)
        elif conversion == 'a':
            if sys.version_info < (3,):
                return repr(value)
            return ascii(value)
        raise ValueError('Unknown conversion specifier {0!s}'.format(conversion))


class TrailingFormatter(Formatter):
    def format_field(self, value, spec):
        if len(spec) > 1 and spec[0] == 't':
            value = str(value) + spec[1]  # append the extra character
            spec = spec[2:]

        return super(TrailingFormatter, self).format_field(value, spec)


class TrailingLookup:
    def __init__(self, **kw):
        self._lookup = {}
        self._lookup.update(kw)

    def __getitem__(self, key):
        if key not in self._lookup:
            raise ValueError('no format insert value for key {} specfied'.format(key))
        return self._lookup[key]

    def __setitem__(self, key, value):
        key = str(key)
        if len(key) != 1:
            raise ValueError('key must be exactly one character not "{}"'.format(key))
        self._lookup[key] = value


class TrailingLookupFormatter(Formatter):
    def __init__(self, *args, **kw):
        super(TrailingLookupFormatter, self).__init__(*args)
        self.lookup = TrailingLookup()
        for k in kw:
            self.lookup[k] = kw[k]

    def format_field(self, value, spec):
        if len(spec) > 1 and spec[0] == 't':
            value = str(value) + self.lookup[spec[1]]
            spec = spec[2:]
        return super(TrailingLookupFormatter, self).format_field(value, spec)
