.. py:module:: colda.authorization
.. py:currentmodule:: colda.authorization

:py:mod:`~colda.authorization` Module
==============================

The :py:mod:`~colda.authorization` module contains a class of the same name to
handle simple authentication(login) and authorization(token)

Examples
--------

Login and logout to an account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script shows how to login and logout.

.. code-block:: python

    import colda

    # login
    colda.userLogin('xie1', 'Xie1@123')

    # logout
    colda.userLogout()

.. note::

    The :py:class:`~colda.colda.authorization.authorization` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: colda.authorization.Authorization
    :members: