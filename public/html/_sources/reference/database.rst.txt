.. py:module:: colda.database
.. py:currentmodule:: colda.database

:py:mod:`~colda.database` Module
==============================

The :py:mod:`~colda.database` module contains classes to store
intermediate outputs from algorithm part. 

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

    The :py:class:`~colda.database` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: colda.database.default_database.default_metadata_database.DefaultMetadataDatabase
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: colda.database.test_database.algorithm_database.TestAlgorithmDatabase
   :members:
   :undoc-members:
   :show-inheritance:
.. autoclass:: colda.database.test_database.assistor_metadata_database.TestAssistorMetadataDatabase
   :members:
   :undoc-members:
   :show-inheritance:
.. autoclass:: colda.database.test_database.sponsor_metadata_database.TestSponsorMetadataDatabase
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: colda.database.train_database.algorithm_database.TrainAlgorithmDatabase
   :members:
   :undoc-members:
   :show-inheritance:
.. autoclass:: colda.database.train_database.assistor_metadata_database.TrainAssistorMetadataDatabase
   :members:
   :undoc-members:
   :show-inheritance:
.. autoclass:: colda.database.train_database.sponsor_metadata_database.TrainSponsorMetadataDatabase
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: colda.database.strategy.database_strategy.DatabaseOperator
   :members:
   :undoc-members:
   :show-inheritance: