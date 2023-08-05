import os
import sys
from setuptools import setup, find_packages


if sys.version_info < (2, 7):
    raise NotImplementedError("""\n
##############################################################
# globus-cli does not support python versions older than 2.7 #
##############################################################""")


# single source of truth for package version
version_ns = {}
with open(os.path.join("globus_cli", "version.py")) as f:
    exec(f.read(), version_ns)
version = version_ns['__version__']

setup(
    name="globus-cli",
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'globus-sdk==1.5.0',
        'click>=6.6,<7.0',
        'jmespath==0.9.2',
        'configobj>=5.0.6,<6.0.0',
        'requests>=2.0.0,<3.0.0',
        'six>=1.10.0,<2.0.0',
        # cryptography has unusual versioning and compatibility rules:
        # https://cryptography.io/en/latest/api-stability/
        # we trust the two next major versions, per the Deprecation policy
        #
        # as new versions of cryptography are released, we may need to update
        # this requirement
        'cryptography>=1.8.1,<2.5.0'
    ],

    extras_require={
        # deprecated, but do not remove -- doing so would break installs which
        # are already using this extra
        'delegate-proxy': []
    },

    entry_points={
        'console_scripts': ['globus = globus_cli:main']
    },

    # descriptive info, non-critical
    description="Globus CLI",
    long_description=open("README.rst").read(),
    author="Stephen Rosen",
    author_email="sirosen@globus.org",
    url="https://github.com/globus/globus-cli",
    keywords=["globus", "cli", "command line"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
)
