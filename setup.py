import sys

from setuptools import setup


runtime_deps = []

if sys.version_info < (3, 4):
    runtime_deps.append('enum34 >= 1.0.4')


setup(
    name='httplib3',
    version='0.1',
    install_requires=runtime_deps,
)
