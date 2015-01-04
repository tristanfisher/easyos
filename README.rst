easyos
======

A convenience-dictionary of common operating-system information needed while writing code.

Update 4-Jan 2015: Moved support to Python 3.x

Getting easyos:
---------------

Simply:

.. code-block:: bash

    pip install easyos

Using easyos is easy:

To list all the keys, simply import and print `easyos`:

.. code-block:: python

    $ python
    >>> from pprint import pprint
    >>> from easyos import easyos
    >>> pprint(easyos)
    {'current_gid': 20,
     'current_uid': 501,
     'current_user': 'tfisher',
     'current_user_desktop': '/Users/tfisher/Desktop',
     'current_user_group': 'staff',
     'homedir': '/Users/tfisher',
     'os': 'Darwin',
     'platform': 'Darwin-14.0.0-x86_64-i386-64bit',
     'python_version': '3.4.2',
     'release': '10.10.1',
     'tmp_dir': '/var/folders/k6/dzxr5tss2kn_2tbbk_jfk4c40000gn/T',
     'type': 'Darwin'}
    >>>

To use `easyos` in a script, simply call the relevant key:

.. code-block:: python

    if easyos['os'] == 'Darwin' and easyos['python_version'] == '3.4.2':
        print("Python3 on OS X.")


Abstract away the tedious bits of cross-platform coding:

.. code-block:: python

    with open (easyos['tmp_dir']+'/script', 'w') as log:
        message = "wow that's easy"
        log.write(message)


New features / Pull requests:
-----------------------------

Make a pull request with your change or addition and I'll merge it if nudges the module in the right direction.

As a non-Windows user, I'm unlikely to add more Windows attributes, but if you need something added, simply branch, make a pull request, and I'll likely merge.
