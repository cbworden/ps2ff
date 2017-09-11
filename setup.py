from distutils.core import setup
import os.path

setup(name='ps2ff',
      version=1.1,
      description='Approximated rupture distances from point source',
      author='Eric Thompson, Bruce Worden',
      author_email='emthompson@usgs.gov, cbworden@usgs.gov',
      url='http://github.com/usgs/shakelib',
      packages=['ps2ff'],
      package_data={'ps2ff': [os.path.join('tables', '*')]},
      scripts=['run_ps2ff', 'run_ps2ff_single_event',
               'Cy14HwMeanVar.py', 'HwMeanVar.py'],
      )


