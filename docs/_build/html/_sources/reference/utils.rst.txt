.. py:module:: colda.utils
.. py:currentmodule:: colda.utils

:py:mod:`~colda.utils` Module
==============================

The :py:mod:`~colda.utils` module contains a number of helper functions, such as type checking,
type converting, etc.

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
    
.. note::

    The :py:class:`~colda.utils` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Functions
---------
.. autofunction:: colda.utils.dtypes.convert.to_list
.. autofunction:: colda.utils.dtypes.convert.to_string
.. autofunction:: colda.utils.dtypes.convert.to_tuple
.. autofunction:: colda.utils.dtypes.convert.to_serializable

.. autofunction:: colda.utils.dtypes.convert.is_numpy
.. autofunction:: colda.utils.dtypes.convert.is_dict_like
.. autofunction:: colda.utils.dtypes.convert.is_list_like
.. autofunction:: colda.utils.dtypes.convert.is_tuple
.. autofunction:: colda.utils.dtypes.convert.is_list
.. autofunction:: colda.utils.dtypes.convert.is_integer
.. autofunction:: colda.utils.dtypes.convert.is_float
.. autofunction:: colda.utils.dtypes.convert.is_set
.. autofunction:: colda.utils.dtypes.convert.is_serializable

Classes
-------
.. autoclass:: colda.utils.log.base.BaseLog
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.utils.log.algorithm_log.AlgorithmLog
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: colda.utils.log.workflow_log.WorkflowLog
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.utils.dict_helper.DictHelper
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: colda.utils.serialization.Serialization
    :members:
    :undoc-members:
    :show-inheritance:
