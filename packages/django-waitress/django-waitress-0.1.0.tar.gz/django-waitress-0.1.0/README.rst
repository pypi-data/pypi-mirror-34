django-waitress
===============

Run a production-ready server from manage.py!

This Django app just provides a management command that serves your Django project using Waitress, a production-ready and `Heroku-friendly <heroku>`_ WSGI server.

.. _heroku: http://blog.etianen.com/blog/2014/01/19/gunicorn-heroku-django/

Usage
-----

.. code-block:: sh

    # Serve on http://0.0.0.0:7000
    python manage.py serve --host 0.0.0.0 --port 7000

    # Serve on the Unix socket /var/run/myapp
    python manage.py serve --unix /var/run/myapp

    # Serve on the host defined by WAITRESS_HOST
    # and the port defined by WAITRESS_PORT
    # in settings.py
    # (defaults to localhost:8000)
    python manage.py serve

Alternatives
------------

You could just install Waitress itself, and run the ``waitress-serve`` command it provides, pointing to your ``wsgi.py`` file; the only thing that this project does is provide a Django management command, and remove the need for a ``wsgi.py`` in your project.

License
-------

This project was extracted from `CMV's cookiecutter-django <ccdj>`_

.. _ccdj: https://gitlab.com/abre/cookiecutter-django

.. raw:: html

    <p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
        <a rel="license"
            href="http://creativecommons.org/publicdomain/zero/1.0/">
            <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
        </a>
        <br />
        To the extent possible under law,
        <span resource="[_:publisher]" rel="dct:publisher">
            <span property="dct:title">Commercial Motor Vehicles Pty Ltd</span></span>
        have waived all copyright and related or neighboring rights to
        <span property="dct:title">cookiecutter-django</span>.
        This work is published from:
        <span property="vcard:Country" datatype="dct:ISO3166"
            content="AU" about="[_:publisher]">
        Australia</span>.
    </p>