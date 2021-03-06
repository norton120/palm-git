from distutils.core import setup
from pathlib import Path
import sys

# require version of setuptools that supports find_namespace_packages
from setuptools import setup

try:
    from setuptools import find_namespace_packages
except ImportError:
    # the user has a downlevel version of setuptools.
    print('Error: palm requires setuptools v40.1.0 or higher.')
    print(
        'Please upgrade setuptools with "pip install --upgrade setuptools" and try again'
    )
    sys.exit(1)

# User-friendly description from README.md
this_directory = Path(__file__).parent
long_description = Path(this_directory, 'README.md').read_text()

setup(
    name='palm-git',
    version='0.0.1',
    description='palm-git extension for Palm CLI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ethan Knox',
    author_email='ethan.m.knox@gmail.com',
    url='',
    packages=find_namespace_packages(include=['palm', 'palm.*']),
    package_data={'': ['*.yaml', '*.yml']},
    install_requires=['palm>=2.1.0'],
    license='MIT',
    classifiers=[],
)