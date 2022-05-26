.. py:module:: synspot.StopRequest
.. py:currentmodule:: synspot.StopRequest

:py:mod:`~synspot.StopRequest` Module
==============================

The :py:mod:`~synspot.StopRequest` module contains a class of the same name to
stop the task.

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

    The :py:class:`~synspot.StopRequest.StopRequest` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: synspot.StopRequest.StopRequest
    :members: