"""Setup the posydon package."""

from __future__ import print_function
import glob
import versioneer
import os.path

cmdclass = {}


# VERSIONING

__version__ = versioneer.get_version()
cmdclass.update(versioneer.get_cmdclass())


# TOGGLE WRAPPING C/C++ OR FORTRAN

WRAP_C_CPP_OR_FORTRAN = False

if WRAP_C_CPP_OR_FORTRAN:
    from distutils.command.sdist import sdist

    try:
        from numpy.distutils.core import setup, Extension
    except ImportError:
        raise ImportError("Building fortran extensions requires numpy.")

    cmdclass["sdist"] = sdist
else:
    from setuptools import setup, find_packages


# DOCUMENTATION

# import sphinx commands
try:
    from sphinx.setup_command import BuildDoc
except ImportError:
    pass
else:
    cmdclass["build_sphinx"] = BuildDoc

# read description
with open("README.md", "rb") as f:
    longdesc = "f.read().decode().strip()"


# DEPENDENCIES
if 'test' in sys.argv:
    setup_requires = [
        'setuptools',
        'pytest-runner',
    ]
else:
    setup_requires = []


# These pretty common requirement are commented out. Various syntax types
# are all used in the example below for specifying specific version of the
# packages that are compatbile with your software.
install_requires = [
    'numpy >= 1.16, < 1.20',
    'scipy >= 0.17',
    'iminuit >= 1.3.7',
    'configparser',
    'astropy >= 1.1.1, < 3.0.0 ; python_version < \'3\'',
    'astropy >= 1.1.1 ; python_version >= \'3\'',
    'pandas >= 0.24',
    'scikit-learn == 0.21.3',
    'matplotlib >= 3.0.0',
    'matplotlib-label-lines == 0.3.8',
    'PyQt5 == 5.15.3',
    'h5py == 2.10.0',
    'psutil==5.6.7',
    'tqdm',
    'tables',
]

tests_require = [
    "pytest >= 3.3.0",
    "pytest-cov >= 2.4.0",
]

# For documenation
extras_require = {
    "doc": [
        "matplotlib",
        "ipython",
        "sphinx <= 4.2.0",
        "numpydoc",
        "sphinx_rtd_theme",
        "sphinxcontrib_programoutput",
        "PSphinxTheme",
    ],
    "hpc": ["mpi4py"],
}

# ONLY IF WRAPPING C C++ OR FORTRAN
FORTRAN_SOURCES = [
    "cosmic/src/comenv.f",
    "cosmic/src/corerd.f",
    "cosmic/src/deltat.f",
    "cosmic/src/dgcore.f",
    "cosmic/src/evolv2.f",
    "cosmic/src/gntage.f",
    "cosmic/src/hrdiag.f",
    "cosmic/src/instar.f",
    "cosmic/src/kick.f",
    "cosmic/src/mix.f",
    "cosmic/src/mlwind.f",
    "cosmic/src/mrenv.f",
    "cosmic/src/ran3.f",
    "cosmic/src/rl.f",
    "cosmic/src/star.f",
    "cosmic/src/zcnsts.f",
    "cosmic/src/zfuncs.f",
    "cosmic/src/concatkstars.f",
    "cosmic/src/bpp_array.f",
]

if WRAP_C_CPP_OR_FORTRAN:
    wrapper = Extension('cosmic._evolvebin', sources=FORTRAN_SOURCES,
                        extra_compile_args=["-g"],
                        # extra_f77_compile_args=["-O0"],
                        # extra_f90_compile_args=["-O0"]
                        )


# RUN SETUP

packagenames = find_packages()

# Executables go in a folder called bin
scripts = glob.glob(os.path.join("bin", "*"))

PACKAGENAME = "posydon"
DISTNAME = "posydon"
AUTHOR = "POSYDON Collaboration"
AUTHOR_EMAIL = "scottcoughlin2014@u.northwestern.edu"
LICENSE = "GPLv3+"
DESCRIPTION = "POSYDON the Next Generation of Population Synthesis"
GITHUBURL = "https://github.com/POSYDON-code/POSYDON"

setup(
    name=DISTNAME,
    provides=[PACKAGENAME],
    version=__version__,
    description=DESCRIPTION,
    long_description=longdesc,
    long_description_content_type="text/markdown",
    ext_modules=[wrapper] if WRAP_C_CPP_OR_FORTRAN else [],
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=packagenames,
    include_package_data=True,
    cmdclass=cmdclass,
    url=GITHUBURL,
    scripts=scripts,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    python_requires=">3.5, <4",
    use_2to3=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3+)",
    ],
)
