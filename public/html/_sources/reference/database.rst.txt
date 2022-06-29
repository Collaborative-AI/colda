.. py:module:: colda.database
.. py:currentmodule:: colda.database

:py:mod:`~colda.database` Module
==============================

The :py:mod:`~colda.database` module contains a class of the same name to
handle the database in memory.

Examples
--------

Retrieve history from database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script shows how to retrieve history from database

.. code-block:: python

    import colda
    colda.get_all_task_id_as_sponsor()
    colda.get_all_test_id_as_sponsor()
    colda.get_all_task_id_as_assistor()
    colda.get_all_test_id_as_assistor()

.. note::

    The :py:class:`~colda.colda.database.database` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: colda.database.Database
    :members: