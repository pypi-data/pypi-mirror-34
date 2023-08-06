ein
========

Generic configuration library for any app.

Pretty much a Flask config-like object with added functionality based on flask-appconfig.

Tested with Python 2.7, 3.4, 3.5, 3.6.

|Test Status| |Coverage Status| |Documentation Status|

-  PyPi: https://pypi.python.org/pypi/ein


TODO
----

- Move to explicit usage that accept either files or strings, *not* both.
- Documentation
- Import work using chainmaps to unhackify


Installation
------------

.. code:: sh

    pip install ein


Running tests
-------------

Pytest is the test runner.

Tox is used to handle testing multiple python versions.

.. code:: sh

    tox


.. |Test Status| image:: https://circleci.com/gh/akatrevorjay/ein.svg?style=svg
   :target: https://circleci.com/gh/akatrevorjay/ein
.. |Coverage Status| image:: https://coveralls.io/repos/akatrevorjay/ein/badge.svg?branch=develop&service=github
   :target: https://coveralls.io/github/akatrevorjay/ein?branch=develop
.. |Documentation Status| image:: https://readthedocs.org/projects/ein/badge/?version=latest
   :target: http://ein.readthedocs.org/en/latest/?badge=latest

