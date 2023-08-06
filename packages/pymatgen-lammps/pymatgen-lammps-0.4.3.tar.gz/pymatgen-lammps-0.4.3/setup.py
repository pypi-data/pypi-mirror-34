# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = '0.4.3'
setup(
    name='pymatgen-lammps',
    version=version,
    description='A LAMMPS wrapper using pymatgen',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/costrouc/pymatgen-lammps',
    author='Chris Ostrouchov',
    author_email='chris.ostrouchov+pymatgen-lammps@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='lammps pymatgen wrapper',
    download_url='https://gitlab.com/costrouc/pymatgen-lammps/repository/archive.zip?ref=v%s' % version,
    packages=find_packages(exclude=['docs', 'tests', 'notebooks']),
    install_requires=[
        'pymatgen==2017.7.4',
    ],
    setup_requires=['pytest-runner', 'setuptools>=38.6.0'],  # >38.6.0 needed for markdown README.md
    extras_require={
        'zmq_legos': 'zmq_legos'
    },
    tests_require=['pytest'],
    package_data={'pmg_lammps': ['sets/*.json']},
    entry_points={
        'console_scripts': [
            'pylammps=pmg_lammps.__main__:main'
        ]
    },
)
