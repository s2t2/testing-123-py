

# Testing 1,2,3

An example Python application repository, configured with automated tests and continuous integration.

[![Build Status](https://travis-ci.com/s2t2/testing-123.svg?branch=master)](https://travis-ci.com/s2t2/testing-123)

## Installation

Initialize and activate a new virtual environment:

```sh
conda create -n testing-123-env # first time only
# ...
conda activate testing-123-env
```


From within the virtual environment, install pytest (specifically version 3.10.1, to avoid errors in newer versions):

```sh
pip install pytest==3.10.1
```


## Running Tests

Use pytest to run tests:

```sh
# all tests:
pytest

# or specific tests:
pytest my_test.py
pytest test/
```
