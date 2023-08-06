
## Py3plex installation file. Cython code for fa2 is the courtesy of Bhargav Chippada.
## https://github.com/bhargavchippada/forceatlas2

from os import path
from setuptools import setup,find_packages
from setuptools.extension import Extension

here = path.abspath(path.dirname(__file__))

if path.isfile(path.join(here, 'py3plex/visualization/fa2/fa2util.c')):
    # cython build locally and add fa2/fa2util.c to MANIFEST or fa2.egg-info/SOURCES.txt
    # run: python setup.py build_ext --inplace
    ext_modules = [Extension('py3plex/visualization/fa2.fa2util', ['py3plex/visualization/fa2util.c'])]
    cmdclass = {}
    cythonopts = {"ext_modules": ext_modules,
                  "cmdclass": cmdclass}
else:
    cythonopts = None

    # Uncomment the following line if you want to install without optimizations
    # cythonopts = {"py_modules": ["fa2.fa2util"]}

    if cythonopts is None:
        from Cython.Build import build_ext

        ext_modules = [Extension('py3plex/visualization/fa2.fa2util', ['py3plex/visualization/fa2/fa2util.py', 'py3plex/visualization/fa2/fa2util.pxd'])]
        cmdclass = {'build_ext': build_ext}
        cythonopts = {"ext_modules": ext_modules,
                      "cmdclass": cmdclass}

setup(name='py3plex',
      version='0.4',
      description="A Multilayer network analysis python3 library",
      url='http://github.com/skblaz/py3plex',
      author='Blaž Škrlj',
      author_email='blaz.skrlj@ijs.si',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['rdflib','numpy','networkx','scipy'])
