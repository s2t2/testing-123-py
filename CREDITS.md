# Credits, Notes, Reference

## Pytest Failz

Newest version(s) of pytest either don't recognize tests, or throw
`AttributeError: 'Function' object has no attribute 'get_marker'`. Reverting to a previous stable version solves the problem.

  + https://github.com/pytest-dev/pytest/issues/4608
  + https://github.com/pytest-dev/pytest/releases

> NOTE: `conda search pytest` provides all the available versions of pytest

## Conftest.py Files

By adding a `conftest.py` to the root directory, it allows scripts within the "app" directory (a.k.a. the "app" module) to be imported into tests in the "tests" directory like `from app._______ import _____`.

  + https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files
  + https://pytest.readthedocs.io/en/latest/plugins.html
