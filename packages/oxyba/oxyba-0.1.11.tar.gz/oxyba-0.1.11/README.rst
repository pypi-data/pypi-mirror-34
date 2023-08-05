oxyba -- my wrapper functions and classes for python
====================================================

The oxyba package contains my wrapper functions and classes.

There is no particular purpose nor structure within this package.
New wrapper functions and classes are just added to main package folder.

I advise against using any of this code in production.  
Just don't.
Feel free to copy code and adjust it to your own needs. 


Installation
------------
Check the source code at https://github.com/ulf1/oxyba

.. code:bash

    pip install oxyba

Load the package
----------------
I am going to use the ox shortcut

.. code:: python

    import oxyba as ox


Versioning
----------
After v0.1.11 the versioning rules changed. 
A version X.Y.Z will have the following meaning.

- X: Major changes for the package
- Y: New function, class, module was added
- Z: Bugfixes, minor changes


Notes to myself
---------------
1. Update setup.py (version, requirements)
2. Update CHANGES.txt (what's added, cahnged, removed?)
3. Run:  python setup.py sdist upload -r pypi
