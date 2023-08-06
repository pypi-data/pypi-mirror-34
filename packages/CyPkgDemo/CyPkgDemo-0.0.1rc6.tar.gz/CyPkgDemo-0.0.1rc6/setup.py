# Cython-Python build script
# ref: https://github.com/cython/cython/wiki/PackageHierarchy

# change this as needed
# libdvIncludeDir = "/usr/include/libdv"

import collections
import os
import subprocess
import sys

from setuptools import find_packages
from setuptools import setup
from setuptools import Extension

# We'd better have Cython installed. If not, for package distributors, C files
# will not be generated; for package users, the pre-generated C files (included
# in source distribution by the package distributor) will be used to compile.
#
# If you are a package distributor and you don't have Cython in your developing
# environment, DO NOT make a built distribution (no .c, .pyx, .so files will be
# included)!
try:
    from Cython.Distutils import build_ext

    USE_CYTHON = True  # bool(os.environ.get("USE_CYTHON"))

except ImportError:
    from setuptools.command.build_ext import build_ext

    USE_CYTHON = False

ext = ".pyx" if USE_CYTHON else ".c"

__version__ = '0.0.1rc6'
SRC = "cypkgdemo"


# ---------------------------------------- Something important ----------------------------------------
# Here we define two variables, `SRC` and `PKG`:
#
# `SRC` is the directory of the main package in the source (Note: not the source distribution root -- the level
# where setup.py exists.). The path is relative to the source distribution root.
#
# `PKG` is the name of the main package in the "root" package, i.e. the name to be used when we want to import
# the package after it is installed. (Note again: this may not be equal to `SRC`.)
#
# For a source like
#
#             cython_package_demo
#                     |
#                     +--- src (to be installed as "cypkgdemo", i.e. we want to use it by `import cypkgdemo.atoi`)
#                     |     +--- __init__.py
#                     |     +--- atoi.py
#                     |     +--- ...
#                     |
#                     +--- setup.py
#                     +--- ...
#
# SRC = 'src' and PKG = 'cypkgdemo'.
#
# For pure python project, this is OK --- set `package_dir={PKG: SRC}` in setup() (see 'packemo' as an example).
# But for projects where cython files exist, we must set SRC == PKG. The reason is that when cythonizing and compiling,
# the compiler must know the correct path of .pxd files (therefore expressed with `SRC`), which is pointed out
# by cimport in .pyx files and must be consistent with the package name for the after-installation use (therefore
# expressed with `PKG`). The two expressions must be equal, so `SRC` must be the same with `PKG`.
#
# You can rename the folder 'cypkgdemo' to 'src' and uncomment the lines wrapped with a WARNING, and try
# `python setup.py build_ext / install`, and you will see a compilation error (if all imports in the source code still
# use `PKG`, i.e. from cypkgdemo.atoi cimport ...).
# If you set all imports in the source code to use `SRC` meanwhile (i.e. from src.atoi cimport ...),
# thing will be muuuuuuuch more complicated...
#
# (DO NOT MAKE THINGS COMPLICATED... PLEASE ENJOY YOUR LIFE.)

# # WARNING ==========
# SRC = 'src'
# PKG = 'cypkgdemo'
# # WARNING ==========

# ----------------------------------------------------------------------------------------------------


# scan the `SRC` directory for extension source files (.c or .pyx), converting
# them to extension names in dotted notation
def scan_extention_src_in_dir(directory, ext, files=None):
    if files is None:
        files = []
    for _file in os.listdir(directory):
        path = os.path.join(directory, _file)  # like dir/file1.ext
        fname, fext = os.path.splitext(path)
        if os.path.isfile(path) and fext == ext:
            files.append(fname.replace(os.path.sep, "."))  # like dir.file1
        elif os.path.isdir(path):
            scan_extention_src_in_dir(path, ext, files)
    return files


# generate an Extension object from its dotted name
def make_extension(ext_name):
    ext_path = ext_name.replace(".", os.path.sep) + ext  # like dir/file1.pyx
    # # WARNING ==========
    # if PKG != SRC:
    #     new_ext_name_list = ext_name.split(".")[1:]
    #     new_ext_name_list.insert(0, PKG)
    #     ext_name = '.'.join(new_ext_name_list)
    #     print(ext_name)
    # # WARNING ==========
    return Extension(
        ext_name,  # pkg.file1
        [ext_path],  # dir/file1.pyx
        include_dirs=[
            # libdvIncludeDir,
            "."
        ],  # adding the '.' to include_dirs is CRUCIAL!!
        extra_compile_args=["-O3", "-Wall"],
        extra_link_args=['-g'],
        # libraries=["dv", ],
    )


def collect_data_files_in_dir(fileext, directory, packages, files=None):
    """
    Collect all data files whose ext name is `fileext` in a certain directory
    recursively.

    :param fileext: str or list
        The ext name / list of ext names of data files to be collected.
    :param directory: str
        The directory to be scanned. Relative to the package source root.
    :param packages: iterable
        The packages to be distributed.
        Generally generated by setuptools.find_packages().
    :param files: dict
        A map whose keys are packages, and values are lists of data files in
        the corresponding package, e.g.

            {"pkg": ["f1.ext", "f2.ext"], "pkg.subpkg": ["sf1.ext"]}

        which satisfies the format of package_data.

    :return: dict
        The scanned files.

    """
    if files is None:
        files = {}

    if not isinstance(fileext, collections.Iterable):
        fileext = [fileext]

    this_pkg = directory.replace(os.path.sep, ".")
    if this_pkg in packages:
        datafiles_in_this_pkg = []
        subdirs = []
        for _file in os.listdir(directory):
            path = os.path.join(directory, _file)  # like dir/file1.pxd
            _ext = os.path.splitext(_file)[1]
            if os.path.isfile(path) and _ext in fileext:
                datafiles_in_this_pkg.append(_file)  # like file1.pxd
            elif os.path.isdir(path):
                subdirs.append(path)

        if datafiles_in_this_pkg:
            files[this_pkg] = datafiles_in_this_pkg

        for sd in subdirs:
            collect_data_files_in_dir(fileext, sd, packages, files)

        return files


# Collect the .pxd files according to the packages where they exist.
# The returned result is passed to setup.py as the `package_data` parameter.
# `packages` is the list of known packages under `dir`, which can be got by find_packages()
def collect_pxd_in_dir(directory, packages, files=None):
    return collect_data_files_in_dir(".pxd", directory, packages, files)


# get the list of extensions
ext_names = scan_extention_src_in_dir(SRC, ext)

# and build up the set of Extension objects
extensions = [make_extension(name) for name in ext_names]
if USE_CYTHON:
    from Cython.Build import cythonize

    extensions = cythonize(extensions)

# get the packages
packages = find_packages()

# collect the .pxd and .pyx files as package_data
# (If we are making a source distribution (sdist), .pxd, .pyx and .c files will
# be included; if we are building a binary distribution, only .pxd and .so files
# will be included.)
# TODO: maybe we can try MANIFEST.in?
fileext = [".pxd"]
if "sdist" in sys.argv[1:]:
    if len(sys.argv[1:]) == 1:  # python setup.py sdist
        fileext.append(".pyx")
    else:
        subprocess.call([sys.executable, sys.argv[0], 'sdist'])
        sys.argv.remove("sdist")

package_data = collect_data_files_in_dir(fileext, SRC, packages)

# finally, we can pass all this to distutils
setup(
    name="CyPkgDemo",
    version=__version__,

    author="psrit",
    author_email="xiaojx13@outlook.com",
    url="",

    description="A demo of organizing, building and distributing a Python-Cython mixed package.",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',

    packages=packages,
    ext_modules=extensions,
    cmdclass={'build_ext': build_ext},
    # # WARNING ==========
    # package_dir={PKG: SRC},
    # # WARNING ==========

    # Set the .pxd files as package_data.
    # Using package_data to install .pxd files into your site-packages in your
    # setup.py script allows other packages to cimport items from your module
    # as a dependency.
    # E.g. without this line, all .pxd files ('atoi.pxd', 'sin.pxd') in the
    # source will not be installed into site-packages/cypkgdemo/.
    package_data=package_data,

    extras_require={
        'cython': ['cython', ],
    }
)

# Test only
# if __name__ == "__main__":
#     print(pxd_files)
