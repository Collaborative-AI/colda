.. py:module:: synspot.algorithm
.. py:currentmodule:: synspot.algorithm

:py:mod:`~synspot.algorithm` Module
===========================

The :py:mod:`~synspot.algorithm` module provides a class with the same name which is
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

    from synspot import algorithm
    model = Model(task_mode, model_name)
    model.fit(data, target)
    save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'model.pkl'))

.. warning:: This method is experimental.

Functions
---------

.. autofunction:: synspot.algorithm.make_train_local
.. autofunction:: synspot.algorithm.make_test_local
.. autofunction:: synspot.algorithm.make_hash
.. autofunction:: synspot.algorithm.save_match_id
.. autofunction:: synspot.algorithm.make_match_idx
.. autofunction:: synspot.algorithm.make_residual
.. autofunction:: synspot.algorithm.save_residual
.. autofunction:: synspot.algorithm.make_train
.. autofunction:: synspot.algorithm.save_output
.. autofunction:: synspot.algorithm.make_result
.. autofunction:: synspot.algorithm.make_test
.. autofunction:: synspot.algorithm.make_eval
.. autofunction:: synspot.algorithm.makedir_exist_ok
.. autofunction:: synspot.algorithm.save
.. autofunction:: synspot.algorithm.load
.. autofunction:: synspot.algorithm.log
.. autofunction:: synspot.algorithm.parse_idx


