from distutils.core import setup
from setuptools import find_packages
from os.path import join, dirname


def read(fname):
    return open(join(dirname(__file__), fname)).read()


with open(join(dirname(__file__), 'mrainet/_version.py')) as versionpy:
    exec(versionpy.read())

with open('requirements.txt') as reqsfile:
    required = reqsfile.read().splitlines()

setup(
    name='mrainet',
    version=__version__,
    description=("MR acquisition-invariant network."),
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=required,
    url="https://github.com/wmkouw/mrai-net",
    license='Apache 2.0',
    author='Wouter Kouw',
    author_email='wmkouw@gmail.com',
    classifiers=['Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Image Recognition',
                 'License :: OSI Approved :: MIT License',
                 'Development Status :: 3 - Alpha',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6']
)
