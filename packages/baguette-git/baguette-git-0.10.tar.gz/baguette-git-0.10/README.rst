Service managing the GIT repos workflow.


Configuration
=============

Define the **/etc/farine.ini** or override the path using the environment variable **FARINE_INI**:

::

    [DEFAULT]
    amqp_uri=amqp://127.0.0.1:5672/amqp

    [frasage]
    gitolite=/data/gitolite

    [cuisson]
    enabled=true

    [defournement]
    enabled=true


Launch
======

::

    farine --start=frasage
