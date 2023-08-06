[![Build Status](https://travis-ci.org/corpus-tools/graphANNIS-python.svg?branch=develop)](https://travis-ci.org/corpus-tools/graphANNIS-python)

graphANNIS Python Bindings
==========

GraphANNIS is a library for corpus linguistic queries.
This are the Python bindings to its API.

How to compile
---------------

You will need to build and install the graphANNIS library (Rust version) with cargo for your system before you can build the Java project with Maven.

- Install the latest version (at least 1.28.0) of Rust:
- Clone the graphANNIS library from https://github.com/corpus-tools/graphANNIS/
- Execute `cargo build --release` in the cloned repository
- Change to a clone of this graphANNIS Python bindings repository
- Copy the resulting  shared library file `<graphANNIS-repo>/target/release/libgraphannis_capi.so` (`libgraphannis_capi.dylib` under MacOS X and `graphannis_capi.dll` under Windows) to `graphannis/<platform>/` where the platform is one of the following:

| Operating system       | `<platform>`  |
|------------------------|---------------|
| Linux (64 bit)         | linux-x86-64  |
| MacOS X (64 bit)       | darwin-x86-64 |
| Windows (64 bit)       | win32-x86-64  |

- Install you the python packages locally (use Python3) for your current user (remove the `--user` to install it system-wide)
```
python3 setup.py install --user
```

3rd party dependencies
----------------------

- CFFI (http://cffi.readthedocs.org/) MIT License
- networkX (http://networkx.github.io/) BSD License

Author(s)
---------

* Thomas Krause (thomaskrause@posteo.de)
