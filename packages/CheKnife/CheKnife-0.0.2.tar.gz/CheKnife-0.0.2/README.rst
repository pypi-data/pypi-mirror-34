CheKnife
========

Python utilities compilation.

-  Free software: MIT license

Install
=======

-  TODO

Features
========

hashing
-------

.. code:: python

    from CheKnife.hashing import textmd5sum
    textmd5sum('Hello')
    '8b1a9953c4611296a827abf8c47804d7'

Tests
=====

.. code:: bash

    nosetests --with-coverage --cover-inclusive --cover-package=CheKnife --cover-html
