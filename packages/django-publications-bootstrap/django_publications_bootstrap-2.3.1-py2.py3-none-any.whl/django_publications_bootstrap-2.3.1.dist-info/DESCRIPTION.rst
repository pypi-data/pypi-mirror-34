|Python| |Django| |License| |PyPI| |Build Status| |Coverage Status|

Bootstrap-powered scientific publications for Django
====================================================

A Django app for managing scientific publications, providing a
Bootstrap-powered UI.

Screenshots
-----------

|frontend| |backend|

Features
--------

-  automatically creates lists for individual authors and tags
-  BibTex import/export
-  RIS export (EndNote, Reference Manager)
-  unAPI support (Zotero)
-  customizable publication categories/BibTex entry types
-  PDF upload
-  RSS feeds
-  support for images
-  embeddable references
-  in-text citations, inspired by LaTeX
-  automatic bibliography, inspired by LaTeX

Requirements
------------

-  Python >= 3.4
-  Django >= 1.10.8
-  Pillow >= 2.4.0
-  django-countries >= 4.0
-  django-ordered-model >= 1.4.1
-  six >= 1.10.0
-  Bootstrap v4.0.0-beta
-  django-echoices >= 2.2.5

Installation
------------

Using `PyPI <https://pypi.python.org/pypi/django-publications-bootstrap>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Run ``pip install django-publications-bootstrap``.

Using the source code
~~~~~~~~~~~~~~~~~~~~~

1. Make sure ```pandoc`` <http://pandoc.org/index.html>`__ is installed
2. Run ``./pypi_packager.sh``
3. Run
   ``pip install dist/django_publications_bootstrap-x.y.z-[...].wheel``,
   where ``x.y.z`` must be replaced by the actual version number and
   ``[...]`` depends on your packaging configuration

Configuration
~~~~~~~~~~~~~

1. Add ``publications_bootstrap`` to the ``INSTALLED_APPS`` in your
   project's settings (usually ``settings.py``).
2. Add the following to your project's ``urls.py``:

   ::

       url(r'^publications/', include('publications_bootstrap.urls')),

3. Run ``./manage.py migrate publications_bootstrap``.
4. In your project's base template, make sure the following blocks are
   available in the ``<head>`` tag:

   -  ``head``, to provide xml content
   -  ``css``, to provide CSS specific to this application

   The content itself will be inserted in the ``content`` block.

Credits
-------

This is a fork of
`django-publications <https://github.com/lucastheis/django-publications>`__
from `lucastheis <https://github.com/lucastheis>`__.

.. |Python| image:: https://img.shields.io/badge/Python-3.4,3.5,3.6-blue.svg?style=flat-square
   :target: /
.. |Django| image:: https://img.shields.io/badge/Django1.10,1.11,2.0-blue.svg?style=flat-square
   :target: /
.. |License| image:: https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square
   :target: /LICENSE
.. |PyPI| image:: https://img.shields.io/pypi/v/django_publications_bootstrap.svg?style=flat-square
   :target: https://pypi.python.org/pypi/django-publications-bootstrap
.. |Build Status| image:: https://travis-ci.org/mbourqui/django-publications-bootstrap.svg?branch=master
   :target: https://travis-ci.org/mbourqui/django-publications-bootstrap
.. |Coverage Status| image:: https://coveralls.io/repos/github/mbourqui/django-publications-bootstrap/badge.svg?branch=master
   :target: https://coveralls.io/github/mbourqui/django-publications-bootstrap?branch=master
.. |frontend| image:: https://raw.githubusercontent.com/mbourqui/django-publications-bootstrap/media/frontend_small.png
   :target: https://raw.githubusercontent.com/mbourqui/django-publications-bootstrap/media/frontend.png
.. |backend| image:: https://raw.githubusercontent.com/lucastheis/django-publications/media/backend_small.png
   :target: https://raw.githubusercontent.com/lucastheis/django-publications/media/backend.png


