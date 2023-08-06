from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os
import numpy as np


compile_opts_1 = ['-std=c++11', 
				  '-mmacosx-version-min=10.7', 
				  '-ftree-vectorize', 
				  '-mavx', 
				  '-stdlib=libc++']
compile_opts_2 = ['-std=c++11', 
				  '-mmacosx-version-min=10.7', 
				  '-ftree-vectorize', 
				  '-stdlib=libc++', 
				  '-Ofast']


ext_modules=[
              Extension("*",
                    sources=["*.pyx"],
                    extra_compile_args=compile_opts_2,
                    language = "c++",
                    include_dirs=[np.get_include()]
                    )
]

setup(
	name = "Test",
    ext_modules = cythonize(ext_modules)
	)
