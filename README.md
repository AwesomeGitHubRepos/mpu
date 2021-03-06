[![PyPI version](https://badge.fury.io/py/mpu.svg)](https://badge.fury.io/py/mpu)
[![Python Support](https://img.shields.io/pypi/pyversions/mpu.svg)](https://pypi.org/project/mpu/)
[![Documentation Status](https://readthedocs.org/projects/mpu/badge/?version=latest)](http://mpu.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/MartinThoma/mpu.svg?branch=master)](https://travis-ci.org/MartinThoma/mpu)
[![MartinThoma](https://circleci.com/gh/MartinThoma/mpu.svg?style=shield)](https://app.circleci.com/pipelines/github/MartinThoma/mpu)
[![Build Status](https://dev.azure.com/martinthoma/mpu/_apis/build/status/MartinThoma.mpu?branchName=master)](https://dev.azure.com/martinthoma/mpu/_build/latest?definitionId=1&branchName=master)
[![Coverage Status](https://coveralls.io/repos/github/MartinThoma/mpu/badge.svg?branch=master)](https://coveralls.io/github/MartinThoma/mpu?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub last commit](https://img.shields.io/github/last-commit/MartinThoma/mpu)
![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/MartinThoma/mpu/0.23.1)
[![CodeFactor](https://www.codefactor.io/repository/github/martinthoma/mpu/badge/master)](https://www.codefactor.io/repository/github/martinthoma/mpu/overview/master)
[![mutmut](https://pypi.org/project/mutmut/)](https://img.shields.io/badge/mutmut-1417%2F1813-lightgrey)

# mpu
Martins Python Utilities (mpu) is a collection of utility functions and classes
with no other dependencies.

The total size of the package will never be bigger than 10 MB and currently it
is 120 kB in zipped form. This makes it a candidate to include into AWS Lambda
projects.


## Installation

```bash
$ pip install git+https://github.com/MartinThoma/mpu.git
```

It can, of course, also be installed via PyPI.


## Usage

### Datastructures

```python-repl
>>> from mpu.datastructures import EList

>>> l = EList([2, 1, 0])
>>> l[2]
0

>>> l[[2, 0]]
[0, 2]

>>> l[l]
[0, 1, 2]
```

### Shell

To enhance your terminals output, you might want to do something like:

```python
from mpu.shell import Codes

print("{c.GREEN}{c.UNDERLINED}Works{c.RESET_ALL}".format(c=Codes))
```


### Quick Examples

Creating small example datastructures is a task I encounter once in a while
for StackExchange answers.

```python
from mpu.pd import example_df

df = example_df()
print(df)
```

gives

```
     country   population population_time    EUR
0    Germany   82521653.0      2016-12-01   True
1     France   66991000.0      2017-01-01   True
2  Indonesia  255461700.0      2017-01-01  False
3    Ireland    4761865.0             NaT   True
4      Spain   46549045.0      2017-06-01   True
5    Vatican          NaN             NaT   True
```


### Money

```python
import mpu
from fractions import Fraction

gross_income = mpu.units.Money("2345.10", "EUR")
net_income = gross_income * Fraction("0.80")
apartment = mpu.units.Money("501.23", "EUR")
savings = net_income - apartment
print(savings)
```

prints `1375.31 Euro`


### IO

* Download files with [`mpu.io.download(source, sink)`](https://mpu.readthedocs.io/en/latest/io.html#mpu.io.download).
* Read CSV, JSON and pickle with [`mpu.io.read(filepath)`](https://mpu.readthedocs.io/en/latest/io.html#mpu.io.write).
* Write CSV, JSON and pickle with [`mpu.io.write(filepath, data)`](https://mpu.readthedocs.io/en/latest/io.html#mpu.io.read)
