.. -*- coding: utf-8 -*-
.. :Project:   SoL
.. :Created:   ven 13 lug 2018 09:41:17 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2018 Lele Gaifax
..

.. _gestione utenti:

Gestione utenti
---------------

Per interagire con il sistema, cioè per poter inserire nuovi tornei e altre entità, si devono
inserire per proprie *credenziali* nel :ref:`pannello di login <autenticazione>`. Tali
credenziali possono essere fornite dall'*amministratore*, oppure ottenute tramite l':ref:`auto
registrazione <auto-registrazione>`.

.. contents::


Voci del menu
~~~~~~~~~~~~~

Oltre alle :ref:`azioni standard <pulsanti-standard>` il menu contiene queste voci:

:guilabel:`Club`
  Apre la :ref:`gestione dei club <gestione club>` di cui è responsabile l'utente selezionato

:guilabel:`Campionati`
  Apre la :ref:`gestione dei campionati <gestione campionati>` di cui è responsabile l'utente
  selezionato

:guilabel:`Giocatori`
  Apre la :ref:`gestione dei giocatori <gestione giocatori>` di cui è responsabile l'utente
  selezionato

:guilabel:`Valutazioni`
  Apre la :ref:`gestione delle valutazioni <gestione valutazioni glicko>` di cui è responsabile
  l'utente selezionato

:guilabel:`Tornei`
  Apre la :ref:`gestione dei tornei <gestione tornei>` di cui è responsabile l'utente
  selezionato


.. _inserimento e modifica utenti:

Inserimento e modifica
~~~~~~~~~~~~~~~~~~~~~~

.. index::
   pair: Inserimento e modifica; Utenti

Tutti i campi, ad eccezione della :guilabel:`lingua`, sono obbligatori.

Email e password
++++++++++++++++

Queste sono le credenziali che l'utente dovrà inserire nel :ref:`pannello di login
<autenticazione>`. :guilabel:`email` deve essere un indirizzo valido e la :guilabel:`password`
può essere qualunque cosa più lunga di cinque caratteri.

.. note:: Mentre la procedura di :ref:`auto registrazione <auto-registrazione>` accerta la
          validità dell'indirizzo email, quando questo viene inserito o modificato manualmente
          non viene effettuata alcuna verifica che l'indirizzo corrisponda a una casella di
          posta esistente. Si raccomanda pertanto di prestare particolare attenzione: un valore
          sbagliato preclude la possibilità di poter :ref:`reimpostare
          <reimpostazione-password>` la propria password nel caso venisse dimenticata!

Nome e cognome
++++++++++++++

Non possono essere lasciati in bianco.

Lingua
++++++

Se impostata, verrà usata a prescindere dalle impostazioni del browser quando l'utente accede
al sistema.

Gestione responsabilità
+++++++++++++++++++++++

L'*amministratore* può dare il permesso di :guilabel:`gestione responsabilità` a particolari
utenti: quando un utente ha questo permesso è in grado di modificare chi è il responsabile
degli altri elementi (club, tornei, ...), anche di quelli che non gli appartengono.

Stato
+++++

Lo stato corrente dell'utente:

`Registrato`
  la procedura di :ref:`registrazione <auto-registrazione>` non è stata ancora completata: gli
  utenti in questo stato **non** possono accedere al sistema

`Confermato`
  il normale stato di un utente abilitato ad accedere al sistema
