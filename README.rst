Flask-SignIn |build-status| |coverage-status|
=============================================

WORK IN PROGRESS - This will be removed upon first release.

Simplified authentication for Flask with Blueprints for authenticating users both
against local databases and against 3rd party identity providers.

The current providers are:


Planned providers:

* Local - username and password via form data
* Basic - username and password via header
* GitHub - OAuth 2.0 based authentication
* Google - OpenID Connect 1.0 based authentication
* Yahoo - OpenID Connect 1.0 based authentication

If you would like to add a provider please start an issue and make a pull
request.

.. |build-status| image:: https://travis-ci.org/mrshannon/flask-signin.svg?branch=master&style=flat
   :target: https://travis-ci.org/mrshannon/flask-signin
   :alt: Build status
.. |coverage-status| image:: http://codecov.io/github/mrshannon/flask-signin/coverage.svg?branch=master
   :target: http://codecov.io/github/mrshannon/flask-signin?branch=master
   :alt: Test coverage
