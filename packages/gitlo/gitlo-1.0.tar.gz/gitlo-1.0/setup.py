from setuptools import setup
import setuptools

setup(
    name='gitlo',
    version='1.0',
    url="https://github.com/SiddharthShringi/Gitlo",
    author="Siddharth Shringi",
    author_email="siddharthshrigi@gmail.com",
    description="A Command Line Interface for accessing Github api.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    py_modules=['gitlo'],
    install_requires=[
        'Click', 'Requests',
    ],
    entry_points='''
        [console_scripts]
        gitlo=gitlo:cli
    ''',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)
