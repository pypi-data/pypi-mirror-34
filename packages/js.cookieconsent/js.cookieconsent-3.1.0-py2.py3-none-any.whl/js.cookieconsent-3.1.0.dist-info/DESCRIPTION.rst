js.cookieconsent
****************

Introduction
============

This library packages `insites/cookieconsent`_ for `fanstatic`_.

.. _`fanstatic`: http://fanstatic.org
.. _`insites/cookieconsent`: https://github.com/insites/cookieconsent

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js/cookieconsent``) are published to some URL.


How to use?
===========

You can import cookieconsent from ``js.cookieconsent`` and ``need`` it where
you want these resources to be included on a page::

  >>> from js.cookieconsent import cookieconsent
  >>> cookieconsent.need()


.. _`fanstatic`: http://fanstatic.org


CHANGES
*******

3.1.0 (2018-07-18)
==================

- Integrate version 3.1.0 of ``cookieconsent``.




