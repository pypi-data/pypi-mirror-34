.. -*- coding: utf-8 -*-

Changes
-------

4.0a1 (2018-08-06)
~~~~~~~~~~~~~~~~~~

.. warning:: Backward **incompatible** version

   This release uses a different algorithm to crypt the user's password: for this reason
   previous account credentials cannot be restored and shall require manual intervention.

   It's **not** possible to *upgrade* an existing SoL3 database to the latest version.

   However, SoL4 is able to import a backup of a SoL3 database made by ``sol--admin backup``.

* Different layout for matches and results printouts, using two columns for the competitors to
  improve readability (suggested by Daniele)

* New tournaments *retirements policy*

* New "women" and "under xx" tourney's ranking printouts

* New “self sign up” procedure

* New “forgot password” procedure

* New "agreed privacy" on players

* Somewhat prettier “Lit” interface, using `Semantic-UI tables`__

* Technicalities:

  * Development moved to GitLab__

  * Officially supported on Python 3.6 and 3.7, not anymore on <=3.5

  * Shiny new pytest-based tests suite

  * Uses `python-rapidjson`__ instead `nssjson`__, as I officially declared the latter as
    *abandoned*

  * Uses `PyNaCl`__ instead of `cryptacular`__, as the former is much better maintained

  * "Users" are now a separated entity from "players": now the login "username" is a mandatory
    email and the password must be longer than **five** characters (was three before)


__ https://semantic-ui.com/collections/table.html
__ https://gitlab.com/lelix/SoL
__ https://pypi.org/project/python-rapidjson/
__ https://pypi.org/project/nssjson/
__ https://pypi.org/project/PyNaCl/
__ https://pypi.org/project/cryptacular/
