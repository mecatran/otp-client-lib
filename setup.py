"""
@author: Laurent GREGOIRE <laurent.gregoire@mecatran.com>
"""

from setuptools import setup, find_packages
import otpclientlib


setup(
    name='otpclientlib',
    version=otpclientlib.__version__,
    description="OpenTripPlanner client library",
    long_description="An open source library for accessing an OpenTripPlanner server through HTTP",
    url='https://github.com/afimb/opt-client-lib',
    author='AFIMB / CEREMA / MECATRAN',
    author_email='laurent.gregoire@mecatran.com',
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    keywords='OpenTripPlanner OTP library',
    packages=find_packages(),
    install_requires=['requests'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    }
)
