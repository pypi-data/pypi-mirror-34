.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/ericsnth/ckanext-openformat.svg?branch=master
    :target: https://travis-ci.org/ericsnth/ckanext-openformat

.. image:: https://coveralls.io/repos/ericsnth/ckanext-openformat/badge.svg
  :target: https://coveralls.io/r/ericsnth/ckanext-openformat

.. image:: https://pypip.in/download/ckanext-openformat/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-openformat/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-openformat/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-openformat/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-openformat/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-openformat/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-openformat/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-openformat/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-openformat/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-openformat/
    :alt: License

=============
ckanext-openformat
=============
	
------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-openformat:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-openformat Python package into your virtual environment::

     pip install ckanext-openformat

3. Add ``openformat`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------
Configure /etc/ckan/default/production.ini with this configuration:

    # List of allowed file extension in resources
    # (optional, default: csv xls xlsx doc docx pdf xml json)
    ericsnth.ckan.file_extension_allowed = csv xls xlsx doc docx pdf xml json


------------------------
Development Installation
------------------------

To install ckanext-openformat for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/ericsnth/ckanext-openformat.git
    cd ckanext-openformat
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Author
-----------------

Ericson Thomas | https://www.linkedin.com/in/ericsnth

Backend Programmer Satu Data Indonesia, Kantor Staf Presiden RI
