.. contents::


==========
plone.oidc
==========

Pure `OpenID Connect`_ implementation for Plone framework which is 100% comply with `OpenID Connect Core 1.0`_ specifications. More over this product is `Health Relationship Trust Profile for OAuth 2.0`_ complience with, so can be easily adaptable with `HEART`_ ecosystem.


Features
--------

- Dexterity Based Membrane user support.
- Fullly RESTFull API complience
- 100% comply with `HEART`_ ecosystem.



Installation
------------

Install plone.oidc by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plone.oidc


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/nazrulworld/plone.oidc/issues
- Source Code: https://github.com/nazrulworld/plone.oidc
- Documentation: https://docs.plone.org/plone/oidc


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: email@gmail.com


License
-------

The project is licensed under the GPLv2.

.. _`OAuth 2.0`: https://oauth.net/2/
.. _`OpenID Connect`: http://openid.net/connect/
.. _`OpenID Connect Core 1.0`: http://openid.net/specs/openid-connect-core-1_0.html
.. _`HEART`: http://openid.net/wg/heart/
.. _`Health Relationship Trust Profile for OAuth 2.0`: http://openid.net/specs/openid-heart-oauth2-1_0.html