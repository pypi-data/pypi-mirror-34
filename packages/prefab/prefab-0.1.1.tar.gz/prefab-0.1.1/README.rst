Prefab
======

.. image:: https://travis-ci.org/zackhsi/prefab.svg?branch=master
    :target: https://travis-ci.org/zackhsi/prefab

Prefab quickly creates a minimal Python project so you can get coding in
seconds!

.. code-block:: bash

    $ prefab todoapp

    ✨✨ todoapp successfully prefabricated! ✨✨

    To get started, run:

        cd todoapp && pipenv run pytest tests

Prefab requires `pipenv`_.

What's in the box?
------------------

Prefab creates a project that uses:

- `pipenv`_ for dependency management
- `pytest`_ for testing

Project structure
-----------------

.. code-block:: bash

    todoapp/
    ├── Pipfile
    ├── Pipfile.lock
    ├── setup.py
    ├── tests
    │   └── test_main.py
    └── todoapp
        └── main.py

.. _`pipenv`: https://github.com/pypa/pipenv
.. _`pytest`: https://github.com/pytest-dev/pytest
