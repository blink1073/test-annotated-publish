from setuptools import setup
try:
    from Cython.Build import cythonize
    ext_modules = cythonize("test_annotated_publish/helloworld.pyx")
except ImportError:
    ext_modules=[]

setup(
    ext_modules = ext_modules
)