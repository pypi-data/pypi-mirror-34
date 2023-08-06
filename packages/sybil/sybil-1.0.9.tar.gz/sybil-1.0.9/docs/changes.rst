Changes
=======

1.0.9 (1 Aug 2018)
------------------

- Fix for pytest 3.7+.

1.0.8 (6 Apr 2018)
------------------

- Changes only to unit tests to support fixes in the latest release of pytest.

1.0.7 (25 January 2018)
-----------------------

- Literal tabs may no longer be included in text that is parsed by the
  :class:`~sybil.parsers.doctest.DocTestParser`. Previously, tabs were
  expanded which could unpleasant problems.

1.0.6 (30 November 2017)
------------------------

- Fix compatibility with pytest 3.3+.

Thanks to Bruno Oliveira for this fix!

1.0.5 (6 June 2017)
-------------------

- Fix ordering issue that would cause some tests to fail when run on systems
  using tmpfs.

1.0.4 (5 June 2017)
-------------------

- Fix another bug in :class:`~sybil.parsers.codeblock.CodeBlockParser` where
  a :rst:dir:`code-block` followed by a less-indented block would be
  incorrectly indented, resulting in a :class:`SyntaxError`.

1.0.3 (2 June 2017)
-------------------

- Fix bug in :func:`~sybil.parsers.codeblock.CodeBlockParser` where it
  would incorrectly parse indented code blocks.

1.0.2 (1 June 2017)
-------------------

- Fix bug in :func:`~sybil.parsers.codeblock.CodeBlockParser` where it
  would not find indented code blocks.

1.0.1 (30 May 2017)
-------------------

- Fix bug where unicode and byte literals weren't corrected in doctest
  tracebacks, event when :attr:`sybil.parsers.doctest.FIX_BYTE_UNICODE_REPR`
  was specified.

1.0.0 (26 May 2017)
-------------------

- Initial release
