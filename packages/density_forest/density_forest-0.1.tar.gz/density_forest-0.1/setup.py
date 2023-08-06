from setuptools import setup

setup(name='density_forest',
      version='0.1',
      description='Density Forest library for novelty detection and confidence estimation',
      url='https://github.com/CyrilWendl/SIE-Master',
      author='Cyril Wendl',
      author_email='cyrilwendl@gmail.com',
      license='MIT',
      packages=['density_forest', 'baselines', 'helpers', 'keras_helpers'],
      zip_safe=False)