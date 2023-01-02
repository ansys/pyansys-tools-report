# PyAnsys Tools Report

[![PyAnsys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![Python](https://img.shields.io/pypi/pyversions/pyansys-tools-report?logo=pypi)](https://pypi.org/project/pyansys-tools-report/)
[![PyPi](https://img.shields.io/pypi/v/pyansys-tools-report.svg?logo=python&logoColor=white)](https://pypi.org/project/pyansys-tools-report)
[![codecov](https://codecov.io/gh/pyansys/pyansys-tools-report/branch/main/graph/badge.svg)](https://codecov.io/gh/pyansys/pyansys-tools-report)
[![GH-CI](https://github.com/pyansys/pyansys-tools-report/actions/workflows/ci.yml/badge.svg)](https://github.com/pyansys/pyansys-tools-report/actions/workflows/ci.yml)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)

Ansys tool for reporting your Python environment's package versions and hardware resources in a standardized way.

## Table of contents

<!--ts-->
   * [Introduction](#introduction)
   * [Documentation and issues](#documentation-and-issues)
   * [How does it work?](#how-does-it-work)
   * [Installation](#installation)
      * [Offline Installation](#offline-installation)
   * [Rendering the docs](#rendering-the-docs)
   * [Running the tests](#running-the-tests)
   * [Requirements](#requirements)
<!--te-->


## Introduction
The PyAnsys Tools Report is a PyAnsys package to homogenize among all the different repositories
the output of system and environment reports related to Ansys products. Its main goals are:

* Provide an homogeneous output style to system and environment reports.
* Allows for customization when reporting Ansys variables and libraries.

You are welcome to help contribute to it in any possible way. Please submit an issue with
any proposal you may have.

## Documentation and issues

See the [documentation](https://report.tools.docs.pyansys.com/) page for more details.

You are welcome to help contribute to it in any possible way. Please submit
[here](https://github.com/pyansys/pyansys-tools-report/issues) an issue with
any proposal you may have. This is the best place to post questions and code.

## How does it work?
This repository basically contains a simple Python package which you can import as follows
(once installed):

```python
    import ansys.tools.report as pyansys_report
```

Once imported, you can then start playing around with it:

```python
    # Instantiate a "default" Report
    rep = pyansys_report.Report()
```

Refer to the [online documentation](https://report.tools.docs.pyansys.com/) to see the details of the module.

## Installation

This package may be installed following two procedures: either the pip package manager installation or
the manual installation. The process to be followed for each of them is shown in the upcoming sections.

The ``pyansys-tools-report`` package currently supports Python >=3.7 on Windows, Mac OS, and Linux.

### Standard installation
Install the latest release from [PyPi](https://pypi.org/project/pyansys-tools-report) with:

```bash
   pip install pyansys-tools-report
```

Alternatively, install the latest from GitHub via:

```bash
   pip install git+https://github.com/pyansys/pyansys-tools-report.git
```

For a local "development" version, install with (requires pip >= 22.0):

```bash
   git clone https://github.com/pyansys/pyansys-tools-report.git
   cd pyansys-tools-report
   pip install .
```


### Offline installation

If you lack an internet connection on your install machine, the recommended way
of installing PyAnsys Tools Report is downloading the wheelhouse archive from the
[Releases Page](https://github.com/pyansys/pyansys-tools-report/releases) for your
corresponding machine architecture.

Each wheelhouse archive contains all the python wheels necessary to install
PyAnsys Tools Report from scratch on Windows and Linux for Python >=3.7. You can install
this on an isolated system with a fresh python or on a virtual environment.

For example, on Linux with Python 3.7, unzip it and install it with the following:

```bash
   unzip pyansys-tools-report-v0.5.0-wheelhouse-Linux-3.7.zip wheelhouse
   pip install pyansys-tools-report -f wheelhouse --no-index --upgrade --ignore-installed
```

If you're on Windows with Python 3.9, unzip to a ``wheelhouse`` directory and
install using the same command as before.

Consider installing using a [virtual environment](https://docs.python.org/3/library/venv.html).
More information on general PyAnsys development can be found in the
[PyAnsys Developer's Guide](https://dev.docs.pyansys.com/).

## Rendering the docs

In case you were interested in rendering the docs locally, you need to clone the repository and
install the docs requirements first:

```bash
   git clone https://github.com/pyansys/pyansys-tools-report.git
   cd pyansys-tools-report
   pip install -e .[doc]
```

Once you have the requirements, render the docs by running the following:

```bash
   make -C doc html
```

This generates the HTML version of the docs, which you may find in the following directory:

```bash
   cd doc/_build/html
```

You can also clean the build directory by running the following command:

```bash
   make -C doc clean
```

## Running the tests

In case you were interested in running the tests locally, you need to clone the repository and
install the test requirements first:

```bash
   git clone https://github.com/pyansys/pyansys-tools-report.git
   cd pyansys-tools-report
   pip install -e .[test]
```

Once you have the requirements, run the tests by running the following:

```bash
   pytest
```

The ``pyproject.toml`` file already contains some default configuration for running the tests. Please,
take a look at it if you may want to run it with your own configuration.


## Requirements

This Python package does not contain specific requirements files. Instead, its requirements may
be found within the ``pyproject.toml`` file which defines the package. Thus, when the package is
installed it automatically detects the dependencies needed and installs them.
