============
pytest-shell
============

A plugin for testing shell scripts and line-based processes with pytest.

You could use it to test shell scripts, or other commands that can be run
through the shell that you want to test the usage of.

Not especially feature-complete or even well-tested, but works for what I
wanted it for. If you use it please feel free to file bug reports or feature
requests.

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with
`@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

* Easy access to a bash shell through a pytest fixture.
* Set and check environment variables through Python code.
* Automatically fail test on nonzero return codes by default.
* Helpers for running shell scripts.
* Mostly, all the great stuff pytest gives you with a few helpers to make it
  work for bash.


Installation
------------

You can install "pytest-shell" via `pip`_ from `PyPI`_::

    $ pip install pytest-shell

Usage
-----

You can use a fixture called 'bash' to get a shell process you can interact
with.

Test a bash function::

    def test_something(bash):
        assert bash.run_function('test') == 'expected output'

Set environment variables, run a .sh file and check results::

    def test_something(bash):
        with bash(envvars={'SOMEDIR': '/home/blah'}) as s:
            s.run_script('dostuff.sh', ['arg1', 'arg2'])
            assert s.path_exists('/home/blah/newdir')
            assert s.file_contents('/home/blah/newdir/test.txt') == 'test text'

Run some inline script, check an environment variable was set::

    def test_something(bash):
        bash.run_script_inline(['touch /tmp/blah.txt', './another_script.sh'])
        assert bash.envvars.get('AVAR') == 'success'

Use context manager to set environment variables::

    def test_something(bash):
        with bash(envvars={'BLAH2': 'something'}):
            assert bash.envvars['BLAH2'] == 'something'

You can run things other than bash (ssh for example), but there aren't specific
fixtures and the communication with the process is very bash-specific.

TODO
----

* Helpers for piping, streaming.
* Fixtures and helpers for docker and ssh.
* Support for non-bash shells.
* Shell instance in setup for e.g. basepath.


Refactoring TODO
----------------

* Make Connection class just handle bytes, move line-based stuff into an
  intermediary.
* Make pattern stuff work line-based or on multiline streams (in a more
  obvious way than just crafting the right regexes).
* Make pattern stuff work on part of line if desired, leaving the rest.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-shell" is free and
open source software


