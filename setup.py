# coding: utf-8

"""
    domian-paas-sdk-python
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dhicn-domain-paas-sdk-python"
VERSION = "1.0.8"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name=NAME,
    version=VERSION,
    author="dhi",
    author_email="wafe@dhigroup.com",
    url="",
    keywords=["sdk", "python", "domain-paas"],
    install_requires=REQUIRES,
    packages=find_packages(where='src',exclude=["test", "tests"]),
    include_package_data=True,
    long_description=readme,
    package_dir={'':'src'},
    license='MIT'
)
