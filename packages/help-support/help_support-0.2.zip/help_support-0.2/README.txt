This module provides a built-in help() function support for Python ctypes bindings.

Copyright (C) 2018 by Dalen Bernaca

help_support enables you to use help() on modules containing functions from
ctypes linked libraries.
It uses pydoc and it is based on it and tries to emulate the original help() function as much as possible,
but I took some liberties to change the output a little.
Submodules are not shown and the order of presentation is slightly different.

Features it shows (in presented order) are:
    NAME
    FILE
    [MODULE DOCS]
    [DESCRIPTION]
    [CTYPES FUNCTIONS]
    [CTYPES STRUCTURES]
    [PYTHON FUNCTIONS]
    [PYTHON CLASSES]
    [DATA]
    [VERSION]
    [DATE]
    [AUTHOR]
    [CREDITS]

How does it work?

It substitutes __builtin__.help() with a new
_Helper() object that will always call original help() except in cases where
presented object is a module containing ctypes._CFuncPtr i.e. the ctypes function(s) and/or ctypes structure(s)
or the object is one of the listed itself.
All variables containing some other ctypes types are recognized as DATA.

In order for the module to show the output that makes sense your ctypes functions should have
the "__doc__" attribute added with the __doc__ string and properly configured attributes "argtypes" and "restype".

An extra, help_support specific, "argnames" attribute can be added to your ctypes function to improve the representation of the function's arguments.
It is a list containing strings with names of each argument in a row.
If "argnames" is properly specified then help() will show a defined name along with the argument's type.

* Note that defining "argnames" will not have inpact on the function itself.
  It is only used by help_support to make the help() more descriptive and remind
  developers what goes where when the function is called.

Structures can also have a "__doc__" string and they should have the "_fields"_ attribute.

When you are making a ctypes Python bindings, just include the
help_support in your package and keep good documentation
of each function pulled from the DLL/DYLIB/SO and declared structures.

Example:
    # examp_module:
    import ctypes
    import ctypes.util

    import help_support
    del help_support # If you want you can remove it now
                     # to avoid cluttering your globals() namespace.
                     # Once it is called you do not usually need it any more.

    l = ctypes.CDLL(ctypes.util.find_library("c"))

    # Pull the time() function from libc,
    # declare and document it:
    time = l.time
    time.argtypes = []
    #time.argnames = ["c_void"] # The function takes no arguments, but you can trick help_support 
                                # to show something in parenthesis if you want to be consistent with C
                                # If there is/are argument(s) you should put its/their name(s) in "argnames".
    time.restype = ctypes.c_int
    time.__doc__ = "Function that returns a system time in seconds."
    -------------------------------------------
    >>> # Usage:
    >>> import examp_module
    >>> help(examp_module)
    >>> help(examp_module.time)
    >>>

The usage is simple.
Just pack it into your ctypes bindings and import it in every module containing ctypes functions and/or structures.
Users of your package will hardly notice that help() was changed a little and they will be glad it did anyway
because they will be able to use it on your bindings and thus
speed up their development.

The module is not very extensively tested and still may have bugs in getting the documentation,
presenting a proper ctypes type names and help's formatting in general.

The module was tested for Python 2.5, 2.6 and 2.7 on the following platforms:
Ubuntu 16.04, Windows XP and Cygwin.
