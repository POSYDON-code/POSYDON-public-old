.. _install:

############
Installation
############

=========================================
Installing the latest release from GitHub
=========================================

Cloning POSYDON
---------------
Clone the repository in a local directory, e.g. `/home/POSYDON/`.

.. code-block::

    git@github.com:POSYDON-code/POSYDON.git


The directory will contain the following structure:

.. code-block::

    posydon/
    README.md
    setup.py
    etc.

Exporting the global path
-------------------------
Export the global path to the cloned POSYDON (you can add this line to your
.bashrc or .bash_profile.), e.g.

.. code-block::

    export PATH_TO_POSYDON='/home/POSYDON/'

Creating a conda environment
----------------------------

We strongly recommend running POSYDON on a dedicated conda environment. We will
name it `posydon`:

.. code-block::

    conda create -n posydon python=3.7

Make sure you agree to any questions about installing required libraries. To
proceed with the installation, we will need to activate the environment:

.. code-block::

    conda activate posydon

Installing git LFS
------------------
Inside the cloned POSYDON repo run the following command to install and
initialize git LFS (this need to be done only once).

.. code-block::

    conda install git-lfs
    git lfs install

Initialize POSYDON submodules
-----------------------------
There are a few submodules that you should initialize right after cloning.
This command will automatically clone the data submodule, make sure you have
~6GB of free storage space.

.. code-block::

    git submodule init
    git submodule update

Installing POSYDON as an editable package
-----------------------------------------
From the cloned POSYDON directory execute the command. Depending on what you
are doing, you may want to remove the `-e` option, which uses the cloned
version of the repository, rather than make a copy in your conda directory.
This step could take a few minutes as multiple dependencies need to be
installed.

.. code-block::

    pip install -e .

After this procedure, you can use standard python commands to import POSYDON
subpackages and modules in any python script:

.. code-block::

    import posydon.grids.psygrid as PSyGrid
    mygrid = PSyGrid("mygrid.h5")

Installing POSYDON MPI module
-----------------------------
If you plan to run MESA grids or population synthesis with POSYDON on HPC
cluster, then you first need to load an MPI library and install mpi4py with

.. code-block::

    conda install mpi4py
..
    pip install -e .[hpc]


=========================================
Installing POSYDON documentations modules
=========================================

These modules are needed in order to compile the documentation

.. code-block::

    pip install -e .[doc]

To compile the documentation and open the html page do the following

.. code-block::

    cd docs/
    make html
    open _build/html/index.html


Installation Notes/FAQ
----------------------

.. note::

    USING IPYTHON OR JUPYTER-NOTEBOOKS WITH POSYDON ENVIRONMENT

    Please note that using the global instance of the conda jupyter-notebook
    or ipython will most likely fail when trying to use posydon.
    PLEASE explicitly install both into the posydon environment with either

    ``conda install jupyter ipython``

    ``pip install jupyter ipython``
