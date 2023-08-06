
Sil_Agnostic_Field
================== 
Database independent django model field. Returns database safe field while using
non-postgres database engine while maintain fidelity to django.contrib.postres.fields when
using postgres database engine


Motivation
----------

This field will allow tests to run on Sqlite while run in Postgres in production


Installation
------------

:: 
    pip install sil_agnostic_field


Usage
-----

.. code::

    INSTALLED_APPS = (
        ...
        'sil_agnostic_field',
        ...
    )


Example
-------

.. code::

    from django.db.models import Model, TextField
    from sil_agnostic_field.array import AgnosticArrayField
    from sil_agnostic_field.json import AgnosticJSONField


    class ExampleModel(Model):
        item_one = AgnosticArrayField(base_field=TextField(max_length=255))
        item_two = AgnosticJSONField()

        