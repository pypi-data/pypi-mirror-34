mkc
===

Initialize a C++ project with cmake boilerplate.

Installation
------------

From PyPI::

    $ pip install mkc

From the project root directory::

    $ python setup.py install

Usage
-----

Simply run it::

    $ mkc $PROJECT_NAME
    $ mkc $PROJECT_NAME -o $PROJECT_DIR


Use --help/-h to view info on the arguments::

    $ mkc --help
    usage: mkc [-h] [--lib-name LIB_NAME] [--output-dir OUTPUT_DIR] name

    positional arguments:
      name

    optional arguments:
      -h, --help            show this help message and exit
      --lib-name LIB_NAME, -l LIB_NAME
      --output-dir OUTPUT_DIR, -o OUTPUT_DIR


Release Notes
-------------

:0.0.3:
    Readme generator
:0.0.2:
    Basic functionality
:0.0.1:
    Project created
