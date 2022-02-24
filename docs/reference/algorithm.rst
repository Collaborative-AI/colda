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

Open, rotate, and display an image (using the default viewer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script loads an image, rotates it 45 degrees, and displays it
using an external viewer (usually xv on Unix, and the Paint program on
Windows).

.. code-block:: python

    from PIL import Image
    with Image.open("hopper.jpg") as im:
        im.rotate(45).show()

Create thumbnails
^^^^^^^^^^^^^^^^^

The following script creates nice thumbnails of all JPEG images in the
current directory preserving aspect ratios with 128x128 max resolution.

.. code-block:: python

    from PIL import Image
    import glob, os

    size = 128, 128

    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as im:
            im.thumbnail(size)
            im.save(file + ".thumbnail", "JPEG")

The algorithm method
---------------

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


