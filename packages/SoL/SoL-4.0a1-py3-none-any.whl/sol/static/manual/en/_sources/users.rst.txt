.. -*- coding: utf-8 -*-
.. :Project:   SoL
.. :Created:   ven 13 lug 2018 09:40:29 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2018 Lele Gaifax
..

.. _users management:

Users management
----------------

To interact with the system, that is to be able to insert new tournaments and other entities,
one must inserts his *credentials* into the :ref:`login panel <authentication>`. Such
credentials may be either granted by the *administrator*, or by a :ref:`self registration
<signin>`.

.. contents::


Menu actions
~~~~~~~~~~~~

In addition to the :ref:`standard actions <standard actions>` the menu at the top contains the
following items:

:guilabel:`Clubs`
  Opens the :ref:`management of the clubs <clubs management>` which the selected user is
  responsible of

:guilabel:`Championships`
  Opens the :ref:`management of the championships <championships management>` which the
  selected user is responsible of

:guilabel:`Players`
  Opens the :ref:`management of the players <players management>` which the selected user is
  responsible of

:guilabel:`Ratings`
  Opens the :ref:`management of the ratings <glicko ratings management>` which the selected
  user is responsible of

:guilabel:`Tourneys`
  Opens the :ref:`management of the tourneys <tourneys management>` which the selected user is
  responsible of


.. _users insert and edit:

Insert and edit
~~~~~~~~~~~~~~~

.. index::
   pair: Insert and edit; Users

All fields, with the exception of :guilabel:`language`, are mandatory.

Email and password
++++++++++++++++++

These are the *credentials* the user shall insert into the :ref:`login panel <authentication>`.
The :guilabel:`email` must be a valid address and the :guilabel:`password` may be anything
longer than five characters.

.. note:: While the :ref:`self registration <signin>` procedure ascertains the validity of the
          email address, when it is inserted or modified manually no check is done that the
          address corresponds to an existing mailbox. It is therefore recommended to pay
          particular attention: a wrong value precludes the possibility of :ref:`resetting
          <reset-password>` the password should it be forgotten!

First name and last name
++++++++++++++++++++++++

These fields cannot be left empty.

Language
++++++++

If set, this overrides the browser's default when the user logs in.

Owners admin
++++++++++++

The *administrator* can grant a :guilabel:`owners admin` permission to particular users: when a
user has this right he can change the ownership of other items (clubs, tournaments...), even of
those not belonging to him.

Status
++++++

The current status of the user:

`Registered`
  the `self registration <signin>` procedure has not been completed yet: users in this state
  **cannot** log in

`Confirmed`
  this is the normal state for an operational user
