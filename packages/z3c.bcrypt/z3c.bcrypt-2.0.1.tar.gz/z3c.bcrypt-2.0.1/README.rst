============
 z3c.bcrypt
============

.. warning:: z3c.bcrypt has been superseeded with the new version of
            `zope.password`_ as it now includes `bcrypt` support based on
            the well-maintained `bcrypt`_ library. Please don't use
            this package in new projects.

z3c.bcrypt provides `zope.password`_ compatible "password manager" utilities
that use bcrypt (or alternatively pbkdf2) encoding for storing passwords.

Both encoding schemes are implemented in the cryptacular_ library that is
a dependency for this package.

.. _`zope.password`: https://pypi.org/project/zope.password/
.. _cryptacular: https://pypi.org/project/cryptacular/
.. _`bcrypt`: https://pypi.org/project/bcrypt/
