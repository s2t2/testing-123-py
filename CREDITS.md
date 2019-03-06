# Credits, Notes, Reference

## Pytest Failz

Newest version(s) of pytest either don't recognize tests, or throw
`AttributeError: 'Function' object has no attribute 'get_marker'`. Reverting to a previous stable version solves the problem.

  + https://github.com/pytest-dev/pytest/issues/4608
  + https://github.com/pytest-dev/pytest/releases

> NOTE: `conda search pytest` provides all the available versions of pytest
