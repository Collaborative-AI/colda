.. py:module:: colda.authentication
.. py:currentmodule:: colda.authentication

:py:mod:`~colda.authentication` Module
==============================

The :py:mod:`~colda.authentication` module contains class to
handle authorization(login) and authentication(token)

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

    The :py:class:`~colda.authentication.authentication` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: colda.authentication.Authentication
    :members:
    :undoc-members:
    :show-inheritance: