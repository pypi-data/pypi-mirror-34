pybashcomplete
==============

Bash completion utility for python scripts

Installation
------------

Install with pip, then install bash completion config::

    $ pip install pybashcomplete

Or for the latest, run from the project root directory::

    $ python setup.py install

To install the bash completion script into /etc/bash_completion.d/pybashcomplete, you will need 
to run the install script with sudo or root::

    $ sudo pybashcomplete-install

After install, you will have to source the file manually::

    $ . /etc/bash_completion.d/pybashcomplete

Usage
-----

Simply run a python script and use tab completion::

    $ python test.py --deb[TAB]
    $ python test.py --debug

    $ python test.py --d[TAB][TAB]
    --debug --demo
    $ python test.py --d


Release Notes
-------------

:0.0.3:
    Made installation script for bash completion script
:0.0.2:
    Fixed a few initial bugs
:0.0.1:
    Project created
