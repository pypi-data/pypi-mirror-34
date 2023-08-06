from distutils.core import setup

from config import __version__

setup(
    name = "config",
    description=("A hierarchical, easy-to-use, powerful configuration "
                 "module for Python"),
    long_description=("This module allows a hierarchical configuration "
                      "scheme with support for mappings and sequences, "
                      "cross-references between one part of the configuration "
                      "and another, the ability to flexibly access real Python "
                      "objects without full-blown eval(), an include facility, "
                      "simple expression evaluation and the ability to change, "
                      "save, cascade and merge configurations. Interfaces "
                      "easily with environment variables and command-line "
                      "options."),
    license=("Copyright (C) 2004-2016 by Vinay Sajip. All Rights Reserved. See "
             "LICENSE for license."),
    version = __version__,
    author = "Vinay Sajip",
    author_email = "vinay_sajip@red-dove.com",
    maintainer = "Vinay Sajip",
    maintainer_email = "vinay_sajip@red-dove.com",
    url = "http://www.red-dove.com/python_config.html",
    py_modules = ["config"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
    ],
    platforms='any',
)
