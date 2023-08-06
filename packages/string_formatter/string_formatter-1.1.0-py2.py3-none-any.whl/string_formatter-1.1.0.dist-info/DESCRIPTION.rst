
################
string_formatter
################

.. image:: https://bitbucket.org/ruamel/string_formatter/raw/default/_doc/_static/license.svg
   :target: https://opensource.org/licenses/MIT

.. image:: https://bitbucket.org/ruamel/string_formatter/raw/default/_doc/_static/pypi.svg
   :target: https://pypi.org/project/string_formatter/

.. image:: https://bitbucket.org/ruamel/oitnb/raw/default/_doc/_static/oitnb.svg
   :target: https://bitbucket.org/ruamel/oitnb/


This package is a back-port of ``string.Formatter`` and its tests
to Python 2.7 and 3.3 (and 3.4.0 as shipping with Ubuntu 14.04
LTS/Linux Mint 17)

It allows empty keys in format strings as introduced in Python 3.4.1, and
fixes a bug ( ``"{:<{}} {}"`` ) when using nested empty keys, that is
available in all versions of ``string.Formatter()`` allowing empty keys (up
to at least 3.5.0rc3).

Usage
=====

The package can be used as a replacement for ``string``::

    import string_formatter as string

Trailing(Lookup)Formatter
=========================

Additionally this package includes two additional formatters ``TrailingFormatter`` and
``TrailingLookupFormatter``.

TrailingFormatter
+++++++++++++++++

``TrailingFormatter``allows a type specification ``t`` with a single
character parameter.  That parameter will be added to the (stringified)
value before applying (left-aligned) formatting. This way it is
possible to add a trailing colon directly attached to a key::

  import string_formatter as string

  fmt = string.TrailingFormatter()
  d = dict(a=1, bc=2, xyz=18)
  for key in sorted(d):
      print(fmt.format("{:t{}<{}} {:>3}", key, ':', 15, d[key]))


giving::

  a:                1
  bc:               2
  xyz:             18


because of the formatting internals, this is however restricted to inserting a
single character.

TrailingLookupFormatter
+++++++++++++++++++++++

``TrailingLookupFormatter`` works similar to ``TrailingFormatter``,
but instead of inserting the character, the character looked up in a
mapping that is part of the formatter. This lookup can be set by
providing parameters at the time of instantiation, or at a later
point. (In the following example named fields are used, but this works
with empty fields as well.)

::

  from string_formatter import TrailingLookupFormatter

  fmt = TrailingLookupFormatter(p='(parenthesis)')
  fmt.lookup['s'] = '[square-brackets]'
  fmt.lookup['c'] = '{curly-braces}'

  for x in 'psc':
      print(fmt.format("{fun:t{t}<{width}} by using{t:>2}", 
                       fun=x.upper()*3,t=x, width=25))


giving::

  PPP(parenthesis)          by using p
  SSS[square-brackets]      by using s
  CCC{curly-braces}         by using c


