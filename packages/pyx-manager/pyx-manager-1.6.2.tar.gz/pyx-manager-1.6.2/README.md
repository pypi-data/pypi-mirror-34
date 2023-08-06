# Pyx, the task-oriented project manager

This project was primarily inspired by [mix](https://hexdocs.pm/mix/Mix.html), project management tool for Elixir projects.
It provides generic tasks for creating, testing, and running projects, available as command-line tools.

[Now available on PyPI!](https://pypi.org/project/pyx-manager/)


## Installation

Pyx is now available on PyPI, so you can install it as any other package:

```bash
pip3 install pyx-manager
```

Just run `pyx`:

```bash
$ pyx
The Python task-oriented project manager.

Usage:
    pyx 
    pyx <task> [<task_args>...]

Tasks:
  new        Pyx project creation
  run        Pyx project execution
  release    Distribute your project to a PyPI repository
  test       Run tests in a Pyx project.
  version    Pyx project version managemen
```


## Project management

You can create a new project with the following command:

```bash
pyx new my_project
```

This will create the following directory:

```txt
my_project/
├── my_project
│   ├── __init__.py
│   └── setup.py
├── .gitignore
├── Pipfile
├── .pyx
│   ├── app.py
│   └── config
│       └── default.py
├── README.md
└── test
    └── test_my_project.py
```

Let's have a look at this.
Your code goes in the directory named after your project; here it's `./my_project/`.
The reason behind this is that `pyx` will help you build your project as a package.

The entry point of a Pyx project is `pyx_app.py`.
It will be run when calling `pyx run` at the root of the project.
It contains a class extending `pyx.Application`, and receiving a `pyx.Config` instance as argument.

The configuration files are modules located in `./config/`, where you will find a default config named `./config/default.py`.
These can contain all one needs to define what an environment is.
Then, one can select with which config to run the project, by running `pyx run <config>`.

The `test` directory is where unit tests files should be placed.
There's already one provided, `./test/test_my_project.py`.
The unit tests are run with `pyx test`, which will call the `unittest` module.

The project also contains a `README.md` and a `.gitignore` files, for git projects.

The structure of such a project might seem to impose a strong dependency to `pyx`;
however, the integrality of your project will be written as a standalone package.
What Pyx brings you is an environment around that package, and convenient tools for managing it as a whole project.
