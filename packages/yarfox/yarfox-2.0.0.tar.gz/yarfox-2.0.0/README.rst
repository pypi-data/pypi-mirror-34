yarfox: Cross post from Mastodon to twitter
===========================================

Install
-------

Get ``Python3`` and insall ``yarfox`` with ``pip``.

Usage
-----

First, run ``yarfox setup`` and follow the instructions. This only needs to be done once.

Then:

* Run ``yarfox fetch`` to fetch your latest toots
* Run ``yarfox publish`` to cross post those toots to twitter

``yarfox publish`` will present every toot in order, asking you wether you want to  publish, skip, or edit them.

You can also run ``yarfox publish`` with the ``--batch`` option to automate the process (for instance in a ``cron`` job  or a ``systemd`` timers).

Enjoy!

Notes
-----

All the data fetched from Mastodon will be stored as plain JSON files inside ``~/.local/share/yarfox``, so you can
also use ``yarfox`` as some sort of backup.
