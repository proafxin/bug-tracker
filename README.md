# Bug Tracker

[![Tox and Trunk](https://github.com/proafxin/bug-tracker/actions/workflows/python-package.yml/badge.svg?branch=develop)](https://github.com/proafxin/bug-tracker/actions/workflows/python-package.yml)

[![codecov](https://codecov.io/gh/proafxin/bug-tracker/graph/badge.svg?token=WAJ9M1BUL1)](https://codecov.io/gh/proafxin/bug-tracker)

A set of asynchronous APIs to keep track of bugs under stories.

## Setup

First ensure the following variables are present in your system: `MYSQL_DBNAME`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, `MYSQL_PORT`. They should be self-explanatory. Also a database with name `MYSQL_DBNAME` should be available already. Install tox and poetry: `pip install tox poetry`. Run `tox` and see all the tests pass.

## API Docs

Install the project first: `poetry install`. Run migration with alembic: `alembic upgrade head`. Then run the command `uvicorn tracker.main:app --reload` and go to `http://127.0.0.1:8000/docs` to test the APIs. Rest should be self-explanatory.
