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

## Travis CI

  + https://travis-ci.com/
  + https://travis-ci.org/getting_started
  + https://github.com/marketplace/travis-ci
  + https://docs.travis-ci.com/user/tutorial/


If repos don't show up in the Travis interface, visit https://github.com/marketplace/travis-ci and re-configure the service to access "All Repositories" or check the specific repo(s) of interest.

Example .travis.yml for Python:

```yml
language: python
python:
  - "3.7"
install:
   - pip install pipenv
   - pipenv install --dev
script:
  - pytest
env:
  SECRET_KEY: abc123
```

Configuring CI server...

  1. Visit https://travis-ci.com/
  2. Login with GitHub account.
  3. Visit https://travis-ci.com/account/repositories and the "settings" of the repo you'd like to configure. You should see "no builds for this repository"
  4. Add a .travis.yml file and push the changes to the remote repository's master branch.


Hmmm Python 3.7 not available on Travis.

  + https://github.com/travis-ci/travis-ci/issues/9815
  + https://github.com/travis-ci/travis-ci/issues/10312
  + https://docs.travis-ci.com/user/languages/python/

Need to either use "3.7-dev" (older / out of date?), or change/specify the type of server / distribution (`dist: xenial`).
