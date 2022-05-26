.. py:module:: synspot.utils
.. py:currentmodule:: synspot.utils

:py:mod:`~synspot.utils` Module
==============================

The :py:mod:`~synspot.utils` module contains some methods to help main functions.

Examples
--------

Train and save the model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script generates a model based on the task_mode and model_name, then train the model
and save the model at the desginated position.

.. code-block:: python

    from synspot import algorithm
    model = Model(task_mode, model_name)
    model.fit(data, target)
    save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'model.pkl'))
    
.. note::

    The :py:class:`~synspot.utils` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Functions
---------

.. autofunction:: synspot.utils.log_helper
.. autofunction:: synspot.utils.check_json_format
.. autofunction:: synspot.utils.check_status_code
.. autofunction:: synspot.utils.load_json_data
.. autofunction:: synspot.utils.load_file
.. autofunction:: synspot.utils.save_file
.. autofunction:: synspot.utils.handle_Algorithm_return_value
.. autofunction:: synspot.utils.handle_base64_padding
