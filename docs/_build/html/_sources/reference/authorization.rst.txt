.. py:module:: synspot.authorization
.. py:currentmodule:: synspot.authorization

:py:mod:`~synspot.authorization` Module
==============================

The :py:mod:`~synspot.authorization` module contains a class of the same name to
handle simple authentication(login) and authorization(token)

Examples
--------

Login and logout to an account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script shows how to login and logout.

.. code-block:: python

    import synspot

    # login
    synspot.userLogin('xie1', 'Xie1@123')

    # logout
    synspot.userLogout()

.. note::

    The :py:class:`~synspot.synspot.authorization.authorization` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: synspot.authorization.Authorization
    :members: