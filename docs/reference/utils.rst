.. py:module:: colda.utils
.. py:currentmodule:: colda.utils

:py:mod:`~colda.utils` Module
==============================

The :py:mod:`~colda.utils` module contains some methods to help main functions.

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

.. autofunction:: colda.utils.log_helper
.. autofunction:: colda.utils.check_json_format
.. autofunction:: colda.utils.check_status_code
.. autofunction:: colda.utils.load_json_data
.. autofunction:: colda.utils.load_file
.. autofunction:: colda.utils.save_file
.. autofunction:: colda.utils.handle_Algorithm_return_value
.. autofunction:: colda.utils.handle_base64_padding
