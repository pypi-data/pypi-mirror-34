import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


version = '0.3.0'


setup(
    name='dieselhaze',
    version=version,
    author='Kris',
    author_email='31852063+krisfris@users.noreply.github.com',
    description=('Magic utility library'),
    license='MIT',
    keywords='',
    url='https://github.com/krisfris/dieselhaze',
    packages=find_packages(exclude=['docs', 'tests']),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    data_files=[('', ['LICENSE', 'README.md'])],
    install_requires=['pandas']
)
