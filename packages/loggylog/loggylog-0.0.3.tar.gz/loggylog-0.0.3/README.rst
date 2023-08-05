loggylog
========

Complex logging, simple API

Installation
------------

From PyPI::

    $ pip install loggylog

From the project root directory::

    $ python setup.py install

Usage
-----

You simply instanciate a logger, and give it a log level.
The log level can either be a string or a list. If it is a string, it will
log that log level or greater, eg. ``'warning'`` specifies warning, critical, or error.

If you use a list, it will only write those log levels. ``['warning']`` would only write
warning level log messages to that file.

Specifying a string with comma separated values like ``'info,error'`` is equivalent to
using ``['info', 'error']``, for convenience if passed as a string through the command line.

If ``sudo=True``, it will see if it has permission to write to the path, and if not or if
the file does not exist and it does not have permission to create a file there, it will
ask for sudo permission and chown the file. This has no effect if you already have permission,
but is useful for first time runs of applications that write to ``/var/log/example.log`` but don't 
have permission to.

It also uses the string method ``format`` transparently, so this works as expected::

    >>> log.critical('Approaching {percent:.2%} the speed of light', percent=0.55554)
    'Approaching 55.55% the speed of light'

See the format documentation_ for more examples.

.. _documentation: https://docs.python.org/3.1/library/string.html#format-examples


Example API usage::

    from loggylog import Logger

    log = Logger()
    
    # default is to write all log messages
    log.add_log('./myproject.log')

    # write everything but debug level to ./myproject.log
    log.add_log('./myproject.log', level='info')

    # write error logging to myproject_error.log
    log.add_log('./myproject_error.log', level='error')

    # display to standard out the following log levels
    log.add_log('<stdout>', level=['warning', 'critical', 'error'])

    # 'warning' is the same as ['warning', 'critical', 'error'] or just 'warning'
    # sudo=True will make sure it has permission to write to a file with that
    # path, or get sudo and chown and chmod it appropriately.
    log.add_log('/var/log/myproject.log', level='warning', sudo=True)

    # ['error'] will just write only error logging
    log.add_log('just_errors.log', level=['error'])

    # if for some reason CSV is more convenient than a list...
    log.add_log('info_and_warning.log', level='info,warning')

    # Basic logging
    log.debug('debuggybug')
    log.info('i got something to tell you')
    log.warning('winter is coming')
    log.critical('critical temperature in reactor')
    log.error('sumthin brken')

    # Also, it transparently uses string formatting
    log.info("We're going to build a {}", 'wall')
    log.info("It's going to be {size}", size='yuge')
    # Ordering by integers in braces
    log.critical("{1} for {0}", 'me', 'vote')
    # See https://docs.python.org/3.1/library/string.html#format-examples
    # for more examples.
 
Release Notes
-------------

:0.0.1:
    Project created
