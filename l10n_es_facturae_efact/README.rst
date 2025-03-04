===========================
Envío de Factura-e a e.FACT
===========================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--spain-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-spain/tree/14.0/l10n_es_facturae_efact
    :alt: OCA/l10n-spain
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-spain-14-0/l10n-spain-14-0-l10n_es_facturae_efact
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/189/14.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

Este módulo permitía la gestión del envío de la facturación electrónica española
a el servicio de envío de facturas de Catalunya (e.Fact).

Actualmente solo permite la actualización de estado de las facturas antiguas.
La actualización se produce en un tarea programada que se va ejecutando periodicamente.
Descarga la actualización y la procesa.

Las nuevas sólo deberían enviarse por FACe.

**Table of contents**

.. contents::
   :local:

Installation
============

No se recomienda la instalación de este módulo en nuevas instalaciones.
Se puede utilizar FACe para enviar las facturas a los entes públicos asociados a e.Fact.
Por ello, se considera que este módulo será eliminado en futuras versiones.

Este módulo depende del módulo *l10n_es_facturae_face* y sus dependencias.

Además, depende de las siguientes librerías Python:

* paramiko
* OpenSSL
* xmlsec

Known issues / Roadmap
======================

Este módulo debe eliminarse a partir de la versión 15 o 16.

Debido a como se procesan las facturas desde e.Fact, se pueden enviar directamente a
FACe.
Luego, el propio e.Fact las recoge de allí y las envía al ente correspondiente.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-spain/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-spain/issues/new?body=module:%20l10n_es_facturae_efact%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Creu Blanca

Contributors
~~~~~~~~~~~~

* Enric Tobella <etobella@creublanca.es>
* `Tecnativa <https://www.tecnativa.com>`__:

  * Pedro M. Baeza

* Lois Rilo <lois.rilo@forgeflow.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-etobella| image:: https://github.com/etobella.png?size=40px
    :target: https://github.com/etobella
    :alt: etobella

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-etobella| 

This module is part of the `OCA/l10n-spain <https://github.com/OCA/l10n-spain/tree/14.0/l10n_es_facturae_efact>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
