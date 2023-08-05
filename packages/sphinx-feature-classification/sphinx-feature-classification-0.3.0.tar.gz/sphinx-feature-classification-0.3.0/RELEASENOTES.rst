=============================
sphinx-feature-classification
=============================

.. _sphinx-feature-classification_0.3.0:

0.3.0
=====

.. _sphinx-feature-classification_0.3.0_New Features:

New Features
------------

.. releasenotes/notes/support-driver-notes-b73d5b185f05db7f.yaml @ b'c07a2e9cf61e749a4e002df1bf1867b86bd9a427'

- You can now specify ``driver-notes.XXX`` values. These are useful to
  provide additional context for features with a status of ``partial``. For
  example::
  
      [operation.Cool_Feature]
      title=Cool Feature
      status=optional
      notes=A pretty darn cool feature.
      driver.foo=complete
      driver.bar=partial
      driver-notes.bar=Requires hardware support.

