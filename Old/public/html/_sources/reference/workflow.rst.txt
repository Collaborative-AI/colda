.. py:module:: colda.workflow
.. py:currentmodule:: colda.workflow

:py:mod:`~colda.workflow` Module
==============================

The :py:mod:`~colda.workflow` module manages the workflow of cooperation
between the sponsor and assistor.

Examples
--------

Initiate a testing task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script shows how to initiate a testing task

.. code-block:: python

    import colda
    # login
    colda.userLogin('xie1', 'Xie1@123')
    
    colda.callForTest(task_id: str, test_file_path: str, test_id_column: str, test_data_column: str, 
                            test_target_column: str, test_name: str=None, test_description: str=None)

.. note::

    The :py:class:`~colda.workflow` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.


Classes
-------

.. autoclass:: colda.workflow.base.BaseWorkflow
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.test_main_workflow.TestMainWorkflow
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.train_main_workflow.TrainMainWorkflow
    :members:
    :undoc-members:
    :show-inheritance:


.. autoclass:: colda.workflow.test_workflow.test_base.TestBaseWorkflow
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.test_workflow.assistor.match_identifier.TestAssistorMatchIdentifier
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.test_workflow.assistor.request.TestAssistorRequest
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.workflow.test_workflow.sponsor.find_assistor.TestSponsorFindAssistor
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.test_workflow.sponsor.match_identifier.TestSponsorMatchIdentifier
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.test_workflow.sponsor.output.TestSponsorOutput
    :members:
    :undoc-members:
    :show-inheritance:


.. autoclass:: colda.workflow.train_workflow.train_base.TrainBaseWorkflow
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.train_workflow.assistor.match_identifier.TrainAssistorMatchIdentifier
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.train_workflow.assistor.request.TrainAssistorRequest
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.train_workflow.assistor.situation.TrainAssistorSituation
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.workflow.train_workflow.sponsor.find_assistor.TrainSponsorFindAssistor
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.train_workflow.sponsor.match_identifier.TrainSponsorMatchIdentifier
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.train_workflow.sponsor.output.TrainSponsorOutput
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.workflow.train_workflow.sponsor.situation.TrainSponsorSituation
    :members:
    :undoc-members:
    :show-inheritance:
