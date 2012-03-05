from distutils.core import setup, Extension

module1 = Extension('cstring_dist',
                    sources = ['src/string_distmodule.c'])

setup (name = 'Auditor',
       version = '1.0',
       description = '',
       packages = ['auditor','auditor.plugins'],
       py_modules = ['main','log','settings'],
       package_data={'auditor.plugins': ['exif.py2','stop.txt']},
       ext_package = "auditor",
       ext_modules = [module1])
