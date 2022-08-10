Installation
============

Warnings
--------

.. warning:: No Warnings

Python Support
--------------

colda supports these Python versions.

+----------------------+-----+-----+-----+-----+-----+-----+-----+-----+
|        Python        |3.10 | 3.9 | 3.8 | 3.7 | 3.6 | 3.5 | 3.4 | 2.7 |
+======================+=====+=====+=====+=====+=====+=====+=====+=====+
| colda >= 0.0.0     | Yes | Yes | Yes | Yes |     |     |     |     |
+----------------------+-----+-----+-----+-----+-----+-----+-----+-----+


Basic Installation
------------------

.. note::

    The following instructions will install colda with support for
    most common image formats. See :ref:`external-libraries` for a
    full list of external libraries supported.

Install colda with :command:`pip`::

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade colda


Windows Installation
^^^^^^^^^^^^^^^^^^^^

We provide colda binaries for Windows compiled for the matrix of
supported Pythons in both 32 and 64-bit versions in the wheel format.
These binaries include support for all optional libraries except
libimagequant and libxcb. Raqm support requires
FriBiDi to be installed separately::

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade colda

To install colda in MSYS2, see `Building on Windows using MSYS2/MinGW`_.


macOS Installation
^^^^^^^^^^^^^^^^^^

We provide binaries for macOS for each of the supported Python
versions in the wheel format. These include support for all optional
libraries except libimagequant. Raqm support requires
FriBiDi to be installed separately::

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade colda

Linux Installation
^^^^^^^^^^^^^^^^^^

We provide binaries for Linux for each of the supported Python
versions in the manylinux wheel format. These include support for all
optional libraries except libimagequant. Raqm support requires
FriBiDi to be installed separately::

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade colda

Most major Linux distributions, including Fedora, Ubuntu and ArchLinux
also include colda in packages that previously contained PIL e.g.
``python-imaging``. Debian splits it into two packages, ``python3-pil``
and ``python3-pil.imagetk``.

