SUMNDX -- Quick summary of a Gromacs index file
===============================================

[![PyPI version](https://badge.fury.io/py/sumndx.svg)](https://badge.fury.io/py/sumndx)

Given a Gromacs index file, SUMNDX displays the name and size of the groups.
The program takes the path of an index file as an argument. If no argument is
provided, then the file is read from the standard input.

Usage
-----

```
sumndx index.ndx
sumndx < index.ndx
cat index.ndx | sumndx
```

Example output
--------------

```
0	System	60534
1	Other	60534
2	F216	1944
3	POPC	14976
4	W	42305
5	WF	1309
6	W_WF	43614
```

Installation
------------

SUMNDX does not require to be installed: once the `sumndx` script is
downloaded, it can be executed directly. However, SUMNDX can be installed using
`pip`:

```
pip install sumndx
```

It is possible to install SUMNDX from github using `pip`:

```
pip install git+https://github.com/jbarnoud/sumndx.git
```

[![Build Status](https://travis-ci.org/jbarnoud/sumndx.svg?branch=master)](https://travis-ci.org/jbarnoud/sumndx)
