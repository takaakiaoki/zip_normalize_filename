import sys
import os
from distutils.core import setup

try:
    import py2exe
except ImportError:
    print('warnig: import py2exe failed.')


vars = {'__version__':'0.1.0'}

setup(name = "zip_normalize_filename",
    version = vars['__version__'],
    description = "normalize filename in zip to utf8 NFC",
    author = "Takaaki AOKI",
    author_email = "aoki.takaaki@gmail.com",
    url = "not yet",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = [],
    package_dir = {},
    package_data = {},
    #'runner' is in the root.
    scripts = ["zip_normalize_filename.py"],
    long_description = """ """,
    # py2exe option
    console=[{'script':"zip_normalize_filename.py"}],
    options={'py2exe':{
        'packages':['zipfile'],
        'bundle_files':2,
        'optimize':2,
        'dist_dir':'dist/zip_normalize_filename-{0:s}'.format(vars['__version__'])}},
    zipfile=None
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []
) 
