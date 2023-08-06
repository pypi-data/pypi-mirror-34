gtsrvd
======

.. image:: https://badge.fury.io/py/gtsrvd.png
    :target: https://badge.fury.io/py/gtsrvd

.. image:: https://travis-ci.org/narfman0/gtsrvd.png?branch=master
    :target: https://travis-ci.org/narfman0/gtsrvd

Ever want to host a localhost server on the public internet, but
can't easily or conveniently punch through your NAT? Yes, that aspect of the
future is broken. OR IS IT..?!

gtsrvd seeks to solve this problem in a similar way as ngrok or serveo.
By a simple command, we acquisition a subdomain, set up a proxy, and
host content to the public internetz. How is this? Well firstly, you do it,
we just automate it :). You host a box (ec2?) on your favorite cloud provider,
run what should be a broadly well known ssh command, and you win!

Installation
============

Currently we rely on nginx, so install and start that service. Then::

    pip install gtsrvd

Getting started
===============

You'll need your cloud provider keys set up so the daemon can acquire
subdomains and route properly. Assuming a domain of `blastedstudios.com`,
from hapless host (behind NAT) connect to `publicbox` with::

    ssh -R 8080:localhost:80 gtrkt@publicbox.blastedstudios.com

from publicbox (with public port 80) run::

    gtsrvd-create --domain blastedstudios.com --subdomain test1 --port 8080

This should create a subdomain gtrkt.blastedstudios.com, then traffic will
flow to your proxy box over ssh to your localhost. What a winner.

Testing
-------

To run unit tests, flake8, and coverage reports, run::

    make test

Deploying
---------

Deploy gtsrvd to your cloud box with suitable roles to allow for subdomain
tweaking. I know you like how it ends in a `d` which implies daemon, so
hopefully soon I'll include the simplistic systemd unit I've used to automate
this, possibly an ansible config and docker container.

TODO
----

* Add paramiko server to auto route & proxy logic
  * Optional: Grab subdomain by username..? (might run command on ssh instead)
* Treat forwarding ssh like the special snowflake it is
* Possibly treat port 80 uniquelly, possible forcing (via cli arg) ssl
* Add ansible/docker support
* Support different clouds (gcp/azure)

LICENSE
-------

Copyright 2018 Jon Robison

See LICENSE file for info
