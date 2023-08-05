A user plugin for helga chat bot
================================

About
-----

Helga is a Python chat bot. Full documentation can be found at
http://helga.readthedocs.org.

This user plugin allows Helga to respond to user-related commands in IRC
and print information about users from LDAP.

::

  03:14 < ktdreyer> helgabot: user adeza
  03:14 < helgabot> adeza is in Remote US GA
  03:14 < helgabot> ktdreyer, it's 5:14pm for adeza (2:00 ahead of your
                    America/Denver timezone)


Installation
------------

This users plugin is `available from PyPI
<https://pypi.python.org/pypi/helga-users>`_, so you can simply install
it with ``pip``::

  pip install helga-users

If you want to hack on the helga-users source code, in your virtualenv
where you are running Helga, clone a copy of this repository from GitHub and
run
``python setup.py develop``.

Configuration
-------------

In your ``settings.py`` file (or whatever you pass to ``helga --settings``),
you must specify a ``LDAP`` dict. For example:

.. code-block:: python

    LDAP = {
        'host': 'ldap.corp.example.com',
        'basedn': 'dc=example,dc=com',
    }


helga-users assumes that this LDAP server host is listening on TCP 389 and
supports STARTTLS.

TODO
----

Some ideas...

We should be able to support more user information sources besides LDAP (for
example, GitHub).

Some type of stronger authentication for users. Integration with NickServ or
IRC ops?

Self-service storage of user credentials for other plugins, using a protected
web form?
