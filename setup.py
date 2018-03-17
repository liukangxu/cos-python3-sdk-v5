from setuptools import setup, find_packages
from platform import python_version_tuple


def requirements():
    with open('requirements.txt', 'r') as fileobj:
        requirements = [line.strip() for line in fileobj]
        return requirements


setup(
    name='cos-python3-sdk-v5',
    version='1.3.2',
    url='https://github.com/liukangxu/cos-python3-sdk-v5',
    license='MIT',
    author='Kangxu Liu, tiedu, lewzylu, channingliu',
    author_email='liukangxu1996@gmail.com',
    description='[UNOFFICIAL] Python 3.5 SDK for Tencent Cloud (QCloud) COS',
    long_description='',
    packages=find_packages(),
    install_requires=requirements()
)
