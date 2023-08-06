from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='density_forest',
      version='0.2',
      description='Density Forest library for novelty detection and confidence estimation',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/CyrilWendl/SIE-Master',
      author='Cyril Wendl',
      author_email='cyrilwendl@gmail.com',
      license='MIT',
      packages=['density_forest', 'baselines', 'helpers', 'keras_helpers'],
      zip_safe=False,
      classifiers=(
          "Programming Language :: Python :: 3"
      ),
      )
