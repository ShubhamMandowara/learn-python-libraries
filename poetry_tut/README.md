### What is poetry?

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

### Why we need poetry in modern development?

To resolve the library versioning issues as there are new versions each day. And it create a virtual environment for you same as conda env


### To install poetry:

    `curl -sSL https://install.python-poetry.org | python3 -`

on linux

### To create new project with poetry:

    `poetry new project_name`

### This will create a directory with project name with
- pyproject.toml
- ReadMe.md
- project_name
    - __init__.py
- tests
    - __init__.py
- poetry.lock

This will create a directory structure

### To initialize poetry in pre existing repository then go to repository and open terminal and type `poetry init` command to initialize the poetry


To add dependencies open terminal :

- Add libery dependencies to poetry
    `poetry add library_name`
- To Remove `poetry remove library_name`
- If there is already a pyproject and poetry.lock file then you can simply type `poetry install`
- To activate poetry env
 `poetry shell`
- To add a libray manually in pyproject add
library_name = version
- We can create different envrionment for development, deployment and for testing
- Can create groups and dependencies to it `poetry add pytest --group test` this is to add dependencies to group test and you can use without `poetry install --without test,docs` to add dependencies to all except the given groups
- Whenever you add a dependency its good to lock them using `poetry lock`


References:
- Install: https://python-poetry.org/docs/
- Basic usage link: https://python-poetry.org/docs/basic-usage/
