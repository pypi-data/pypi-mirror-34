====
cate
====

.. image:: https://gitlab.uni.lu/PCOG/cate/badges/master/pipeline.svg
   :target: https://gitlab.uni.lu/PCOG/cate/commits/master
   :alt: pipeline status

.. image:: https://gitlab.uni.lu/PCOG/cate/badges/master/coverage.svg
   :target: https://gitlab.uni.lu/PCOG/cate/commits/master
   :alt: coverage report

..


CATE stands for Chaotic Attractor TEmplate.

``cate`` is a libre software tool (licensed under GNU Lesser General Public
License v3.0 only) to draw the templates of chaotic attractors.

.. SPDX-License-Identifier: LGPL-3.0-only


Chaotic attractors are solutions of deterministic processes, of which the
topology can be described by templates.  We consider templates of chaotic
attractors bounded by a genus-1 torus described by a linking matrix.

This tool first validates a linking matrix by checking continuity and
determinism constraints.
The tool then draws the template corresponding to the linking matrix, and
optimizes the compactness of the representation.  The representation is saved
as a Scalable Vector Graphics (SVG) file.


Installation
------------

``cate`` is available as a regular Python package.  It hence can easily be
installed with ``pip``.

For more details on how to install a Python package, one can refer to
https://packaging.python.org/tutorials/installing-packages/

The latest stable (recommended) version can be installed with the following
command (assuming ``pip`` is installed):

  .. code-block:: sh

     pip install cate

..

It is recommended to use a virtual environment to install ``cate``.  Again, one
can refer to https://packaging.python.org/tutorials/installing-packages/ to get
a more comprehensive overview.

On a typical Linux environment, the typical commands to use would be:

  .. code-block:: sh

     python3 -m venv cate_venv
     source cate_venv/bin/activate
     pip install cate


This will create a new virtual environment in the ``cate_venv`` subdirectory,
and configure the current shell to use it as the default ``python``
environment.  This will then install ``cate`` in this new environment without
interfering with the already installed packages.

One would then exit this environment either by exiting the current shell, or by
typing the command ``deactivate``.

Further uses of ``cate`` only require to activate the virtual environment with
the following command:

  .. code-block:: sh

     source cate_venv/bin/activate


Usage
-----

The purpose of the ``cate`` is to draw template from a given linking matrix.
For instance, the matrix

.. image:: https://gitlab.uni.lu/PCOG/cate/raw/master/doc/5x5_001_matrix.png
   :target: https://gitlab.uni.lu/PCOG/cate/blob/master/doc/5x5_001_matrix.png
   :align: center
   :scale: 50
   :alt: matrice 5x5

describes a template made of five strips. The matrix has to be written using
JSON format as follows in a file, for instance: `5x5_001.json`

.. code-block:: json

   [[2, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 2]]

A simple example of usage could be: `cate file.json`

.. code-block:: sh

   cate examples/5x5_001.json
   [  INFO  ] Input matrix
   [  INFO  ]   [2, 1, 0, 0, 0]
   [  INFO  ]   [1, 1, 0, 0, 0]
   [  INFO  ]   [0, 0, 0, 0, 0]
   [  INFO  ]   [0, 0, 0, 1, 1]
   [  INFO  ]   [0, 0, 0, 1, 2]
   [  INFO  ] Starting constructing the tree
   [  INFO  ] Maximum possible template length: 2
   [  INFO  ] Finished constructing the tree
   [  INFO  ] Starting creation of the SVG template
   [  INFO  ] Shortest template
   [  INFO  ]   Level 1: (0, 1), (3, 4)
   [  INFO  ] Finished creation of the SVG template


The output is a SVG file (`template.svg`) containing the template.

.. image:: https://gitlab.uni.lu/PCOG/cate/raw/master/doc/5x5_001_template.png
   :target: https://gitlab.uni.lu/PCOG/cate/blob/master/doc/5x5_001_template.png
   :align: center
   :scale: 50
   :alt: template of the matrice 5x5


The comprehensive list of the supported options and their usage is available by
typing ``cate -h``.
