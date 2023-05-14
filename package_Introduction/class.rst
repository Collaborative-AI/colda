.. py:module:: py-pkg.temp
.. py:currentmodule:: py-pkg.temp

:py:mod:`~py-pkg.temp` Module
==============================

The :py:mod:`~py-pkg.temp` module contains a class of the same name to
initiate train stage collaboration.

Examples
--------

Initiate a training task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script shows how to initiate a training task

.. code-block:: python

    import py-pkg
    # login
    py-pkg.userLogin('xie1', 'Xie1@123')
    
    py-pkg.callForTrain(maxRound: int, assistors: list, train_file_path: str, train_id_column: str, train_data_column: str, 
                            train_target_column: str, task_mode: str, model_name: str, metric_name: str, task_name: str=None, task_description: str=None)


.. note::

    The :py:class:`~py-pkg.temp.class_name` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: py-pkg.temp.class_name
    :members: