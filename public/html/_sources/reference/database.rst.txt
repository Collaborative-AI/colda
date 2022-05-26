.. py:module:: synspot.database
.. py:currentmodule:: synspot.database

:py:mod:`~synspot.database` Module
==============================

The :py:mod:`~synspot.database` module contains a class of the same name to
handle the database in memory.

Examples
--------

Retrieve history from database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script shows how to retrieve history from database

.. code-block:: python

    import synspot
    synspot.get_all_task_id_as_sponsor()
    synspot.get_all_test_id_as_sponsor()
    synspot.get_all_task_id_as_assistor()
    synspot.get_all_test_id_as_assistor()

.. note::

    The :py:class:`~synspot.synspot.database.database` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: synspot.database.Database
    :members: