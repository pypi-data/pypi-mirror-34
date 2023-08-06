.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/ericsnth/ckanext-metadata.svg?branch=master
    :target: https://travis-ci.org/ericsnth/ckanext-metadata

.. image:: https://coveralls.io/repos/ericsnth/ckanext-metadata/badge.svg
  :target: https://coveralls.io/r/ericsnth/ckanext-metadata

.. image:: https://pypip.in/download/ckanext-metadata/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-metadata/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-metadata/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-metadata/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-metadata/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-metadata/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-metadata/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-metadata/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-metadata/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-metadata/
    :alt: License

=============
ckanext-metadata
=============

.. Put a description of your extension here:
   CKAN Extension untuk integrasi dengan Portal Satu Data Indonesia v3
   sesuai dengan template DDW 16 field


------------
Installation
------------

.. Add any additional install steps to the list below.

To install ckanext-metadata:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-metadata Python package into your virtual environment::

     pip install ckanext-metadata

3. Add ``metadata`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.metadata --cover-inclusive --cover-erase --cover-tests


-----------------
Author
-----------------

Ericson Thomas | https://www.linkedin.com/in/ericsnth

Programming Specialist Satu Data Indonesia, Kantor Staf Presiden RI
