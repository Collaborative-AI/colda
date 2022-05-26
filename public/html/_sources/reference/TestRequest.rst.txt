.. py:module:: synspot.TestRequest
.. py:currentmodule:: synspot.TestRequest

:py:mod:`~synspot.TestRequest` Module
==============================

The :py:mod:`~synspot.TestRequest` module contains a class of the same name to
initiate test stage collaboration.

Examples
--------

Initiate a testing task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script shows how to initiate a testing task

.. code-block:: python

    import synspot
    # login
    synspot.userLogin('xie1', 'Xie1@123')
    
    synspot.callForTest(task_id: str, test_file_path: str, test_id_column: str, test_data_column: str, 
                            test_target_column: str, test_name: str=None, test_description: str=None)

.. note::

    The :py:class:`~synspot.TestRequest.TestRequest` class has several methods,
    but they are all marked as "experimental." Read that as you will. The
    ``[source]`` link is there for a reason.

.. warning:: This method is experimental.

Classes
-------

.. autoclass:: synspot.TestRequest.TestRequest
    :members: