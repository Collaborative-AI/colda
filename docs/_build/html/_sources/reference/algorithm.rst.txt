.. py:module:: colda.algorithm
.. py:currentmodule:: colda.algorithm

:py:mod:`~colda.algorithm` Module
===========================

The :py:mod:`~colda.algorithm` module provides a class with the same name which is
used to represent a PIL image. The module also provides a number of factory
functions, including functions to load images from files, and to create new
images.

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

Functions
---------

.. autofunction:: colda.algorithm.make_train_local
.. autofunction:: colda.algorithm.make_test_local
.. autofunction:: colda.algorithm.make_hash
.. autofunction:: colda.algorithm.save_match_id
.. autofunction:: colda.algorithm.make_match_idx
.. autofunction:: colda.algorithm.make_residual
.. autofunction:: colda.algorithm.save_residual
.. autofunction:: colda.algorithm.make_train
.. autofunction:: colda.algorithm.save_output
.. autofunction:: colda.algorithm.make_result
.. autofunction:: colda.algorithm.make_test
.. autofunction:: colda.algorithm.make_eval
.. autofunction:: colda.algorithm.makedir_exist_ok
.. autofunction:: colda.algorithm.save
.. autofunction:: colda.algorithm.load
.. autofunction:: colda.algorithm.log
.. autofunction:: colda.algorithm.parse_idx


