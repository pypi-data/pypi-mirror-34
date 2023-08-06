# The pylibcklb library 

[![Python version](https://img.shields.io/pypi/v/pylibcklb.svg)](https://pypi.org/project/pylibcklb/)
[![License](https://img.shields.io/pypi/l/pylibcklb.svg)](https://github.com/Ecklebe/pylibcklb/blob/master/LICENSE.md)         
[![PyPI](https://img.shields.io/pypi/pyversions/pylibcklb.svg)](https://pypi.org/project/pylibcklb/)
[![Build Status](https://gitlab.ecklebe.de/open-source/python/pylibcklb/badges/master/build.svg)](https://gitlab.ecklebe.de/open-source/python/pylibcklb/commits/master) (mirroring, build and install on Linux)

The pylibcklb library an package of different functions and classes for programming in python.

## Requirements

The package was programmed with **python 3.6 64 bit**. Older or newer versions of python were not been tested.

## Installation

To install the package to the python packages you need **pip** the package install management which is included in the python interpreter.

 1. Call the command line under windows as admin
 2. Type the following to command line and that's is

```batch
pip install https://github.com/Ecklebe/pylibcklb/archive/master.zip
```
or 
```batch
pip install pylibcklb
```

## Uninstallation

 1. Call the command line under windows as admin
 2. Type the following to command line and that's is

```batch
pip uninstall pylibcklb
```

## Usage
To use (with caution), simply use this small example:

Write main.py:

```python
# Import of the package functions
from pylibcklb.FunctionLibrary import HelloWorld

# Main fucntion to call with python interpreter
def main():

    # Simple function call
    HelloWorld()

if __name__ == "__main__":
    main()
```

Call the main.py with python from command line:
```batch
python.exe main.py
```
Output of the command line: 

    >>> Hello world i am the pylibcklb package
	
## Changes
For the changes of each version see the [CHANGELOG.md](https://github.com/Ecklebe/pylibcklb/blob/master/CHANGELOG.md) in this folder.

