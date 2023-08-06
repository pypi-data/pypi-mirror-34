.. image:: https://travis-ci.org/nnsnodnb/twitter-oauth-django.svg?branch=travis
    :target: https://travis-ci.org/nnsnodnb/twitter-oauth-django
.. image:: https://coveralls.io/repos/github/nnsnodnb/twitter-oauth-django/badge.svg?branch=travis
    :target: https://coveralls.io/github/nnsnodnb/twitter-oauth-django?branch=travis
.. image:: https://badge.fury.io/py/twitter-oauth-ios-django.svg
    :target: https://pypi.org/project/twitter-oauth-ios-django
.. image:: https://img.shields.io/pypi/pyversions/twitter-oauth-ios-django.svg
   :target: https://pypi.org/project/twitter-oauth-ios-django
.. image:: https://img.shields.io/pypi/wheel/twitter-oauth-ios-django.svg
   :target: https://pypi.org/project/twitter-oauth-ios-django
.. image:: https://img.shields.io/pypi/format/twitter-oauth-ios-django.svg
   :target: https://pypi.org/project/twitter-oauth-ios-django
.. image:: https://img.shields.io/pypi/l/twitter-oauth-ios-django.svg
   :target: https://pypi.org/project/twitter-oauth-ios-django


twitter-oauth-django
====================

Create UserSocialAuth of social_django with OAuth login with twitter-kit-ios.

Supported python versions
-------------------------

3.4, 3.5, 3.6

Supported django versions
-------------------------

2.0.x

Installation
------------

.. code:: bash

    $ pip install twitter-oauth-ios-django

Add ``twitter_oauth_ios`` into ``INSTALLED_APPS`` in your ``settings.py`` file

.. code:: python

    INSTALLED_APPS = [
        ...,
        'social_django',
        'twitter_oauth_ios',
    ]

Add ``twitter_oauth_ios`` routing in ``urls.py`` file

.. code:: python

    from django.urls import include, path

    urlpatterns = [
        ...,
        path('twitter_oauth/', include('twitter_oauth_ios.urls', namespace='twitter_oauth_ios')),
    ]

Sample request
--------------

.. code:: bash

    $ curl -X PUT http://example.com/twitter_oauth/ \
        -H "Content-Type: application/json" \
        -H "Accept: application/json" \
        -d \
        "{
            'user_id': 1111111111,
            'oauth_token': '1111111111-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            'oauth_token_secret': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            'screen_name': 'sample_screen_name',
            'display_name': 'display_name'
         }",

Dependence libraries
--------------------

* Django
* social-auth-app-django

Author
------

nnsnodnb

LICENSE
-------

Copyright (c) 2018 Yuya Oka Released under the MIT license (see `LICENSE <LICENSE>`__)
