import os
from setuptools import setup, find_packages
from pip.req import parse_requirements


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_requirements = parse_requirements('requirements.txt', session=False)

# requirements is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
requirements = [str(ir.req) for ir in install_requirements]


setup(
    name="blockchain-health",
    version="0.0.1",
    author="Dominik Harz",
    author_email="dominik.harz@gmail.com",
    description="A blockchain health monitoring application",
    license="MIT",
    keywords="blockchain monitoring",
    url="",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=requirements,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'venv']),
    scripts=[
        'producers/ethereum/main.py'
    ],
    entry_points={
        'console_scripts': ['producers=producers.ethereum:main'],
    },
)
