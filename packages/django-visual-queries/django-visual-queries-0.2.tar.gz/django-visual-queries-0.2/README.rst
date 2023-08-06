=====
Visual Query Builder
=====

Simple app that provides an admin interface for generating and saving queries based on your defined models.

Quick start
-----------

1. Add "qb" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'qb',
    ]

2. Run `python manage.py migrate` to create the qb models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to start building queries (you'll need the Admin app enabled).

