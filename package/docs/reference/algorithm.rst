.. py:module:: colda.algorithm
.. py:currentmodule:: colda.algorithm

:py:mod:`~colda.algorithm` Module
===========================

The :py:mod:`~colda.algorithm` module provides classes to execute machine learning algorithm. The module also provides a number of factory
functions, including functions to train models, calculate model performance.

Examples
--------

Train and save the model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script generates a model based on the task_mode and model_name, then train the model
and save the model at the desginated position.

.. code-block:: python

    from colda import algorithm
    model = Model(task_mode, model_name)
    model.fit(data, target)
    save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'model.pkl'))

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: colda.algorithm.common_stage.make_dataset.MakeDataset
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.common_stage.make_hash.MakeHash
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.common_stage.make_match_idx.MakeMatchIdx
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.algorithm.test_stage.make_eval.MakeEval
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.test_stage.make_test_local.MakeTestLocal
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.test_stage.make_test.MakeTest
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.algorithm.train_stage.make_residual.MakeResidual
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.train_stage.make_result.MakeResult
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.train_stage.make_train_local.MakeTrainLocal
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.train_stage.make_train.MakeTrain
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.algorithm.metric.metrics.Metric
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.algorithm.model.models.Model
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.algorithm.strategy.custom.test_custom
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.strategy.custom.train_custom
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.algorithm.strategy.test_algorithm
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.algorithm.strategy.train_algorithm
    :members:
    :undoc-members:
    :show-inheritance:

