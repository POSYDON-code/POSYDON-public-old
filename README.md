# POSYDON

POSYDON is a next-generation single and binary-star population synthesis code incorporating full stellar structure and evolution modeling with the use of the MESA code (https://docs.mesastar.org).

POSYDON is being developed by a collaborative team of astrophysicists and computer scientists led by Principal Investigators Tassos Fragos (Université de Genève) and Vicky Kalogera (Northwestern University). The code is modular in many aspects and the user can specify initial population properties and adopt choices that determine how stellar evolution proceeds. Populations are simulated with the use of MESA evolutionary tracks for single, non-interacting, and interacting binaries organized in grids. Machine-learning methods are incorporated and applied on the grids for classification and various interpolation calculations, and the development of irregular grids guided by active learning, for computational efficiency.

## Python distribution and virtual environments
We recommend to install the Python distribution Anaconda and to install POSYDON in a virtual environment. After creating the environment like this
```
conda create -n development python=3.7
```
you can source it with
```
conda activate development
```

## Installing POSYDON


### Cloning POSYDON
Clone the repository in a local directory, e.g. '/home/POSYDON/'. The directory will contain the following structure:
```
posydon/
README.md
setup.py
...
```

### Exporting the global path
Export the global path to the cloned POSYDON (you can add this line to your .bashrc or .bash_profile.), e.g.  
```
export PATH_TO_POSYDON='/home/POSYDON/'
```

### Installing git LFS
Inside the cloned POSYDON repo run the following command to install and initialise git LFS (this need to be done only once).
```
conda install git-lfs
git lfs install
```

### Initialise POSYDON submodules
There are a few submodules that you should initialize right after cloning.
This command will automatically clone the data submodule, make sure you have
~6GB of free storage space.
```
git submodule init
git submodule update
```

### Installing POSYDON as an editable package

From the cloned POSYDON directory execute the command
```
pip install -e .
```
After this procedure, you can import POSYDON subpackages and modules like this:
```
import posydon.grids.psygrid as PSyGrid
mygrid = PSyGrid("mygrid.h5")
```

#### Installing POSYDON MPI module

If you plan to run MESA grids or population synthesis with POSYDON on HPC cluster,
then you first need to load an MPI library and install mpi4py with
```
pip install -e .[hpc]
```

## Installing POSYDON documentations modules

These modules are needed in order to compile the documentation
```
pip install -e .[doc]
```
To compile the documentation and open the html page do the following
```
cd docs/
make html
open _build/html/index.html
```
