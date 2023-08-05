========
Overview
========



Create Markov models trained on Internet Archive text files.

* Free software: BSD license

Installation
============

::

    pip install ia-markov

Quick Start
===========

::

    from ia_markov import Composer

    m = MarkovModel()
    m.train_model('FuturistManifesto')
    m.model.make_sentence()
    'Courage, audacity, and revolt will be drunk with love and admiration for us.'


Documentation
=============

https://python-ia-markov.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


Changelog
=========

0.1.3 (2018-7-22)
-----------------------------------------

* EOL Py2.7 and Windows support
* Fix docs CI build

0.1.2 (2018-7-21)
-----------------------------------------

* Test mocks when downloading corpus
* Deprecate Windows/appveyor support

0.1.1 (2018-7-14)
-----------------------------------------

* Fixed failing flake8 check tests
* Updated travis CI build config

0.1.0 (2016-11-27)
-----------------------------------------

* First release on PyPI.


