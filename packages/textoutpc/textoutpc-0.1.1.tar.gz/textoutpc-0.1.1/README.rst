Planète Casio's textout() BBcode markup language translator
===========================================================

This module contains a BBcode to HTML translator for
`Planète Casio`_. For more information, read the
documentation accessible on `the official website`_.

.. warning::

	If you are accessing this repository from `Planète Casio's forge`_,
	keep in mind that it is only a mirror and that the real repository
	is located `in my forge <Thomas' forge_>`_ for now.

What is left to do
------------------

- Add an ``[imgurl]`` tag.
- Manage blocks superseeding each other;
- Implement BBcode lists using ``[*]``, ``[**]``, …;
- Manage lightscript (or even markdown?) as output languages;
- Check where the errors are to display them to the user:

  * Count character offset, line number and column number in the lexer;
  * Produce readable exceptions;
  * Make a clean interface to transmit them;
- Check why exceptions on raw tags effectively escape the content, as it
  shouldn't…?
- Implement the ``inline`` tweak in order not to read blocks in the
  translator.
- Look for security flaws (we really don't want stored XSS flaws!).
- Manage keywords with tags such as ``[tag key=value other="something else"]``.

.. _Planète Casio:: https://www.planet-casio.com/
.. _Planète Casio's forge:: https://gitea.planet-casio.com/
.. _Thomas' forge_:: https://forge.touhey.fr/pc/textout.git
.. _the official website:: https://textout.touhey.fr/
