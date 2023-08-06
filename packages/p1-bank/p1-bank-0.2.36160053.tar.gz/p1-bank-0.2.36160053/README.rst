================
Django Banks
================

A Django application that provides Indonesian bank choices for use with forms
and a country field for models.

.. contents::
    :local:
    :backlinks: none


Installation
============

1. ``pip install p1-bank``
2. Add ``bank`` to ``INSTALLED_APPS``
3. Run `python manage.py migrate` to create banks models

Bank Model
===========

A model of bank that holds all banks in Indonesia.

Supports long name, short name, bank code, and branch code.

.. code:: python

    >>> from django.apps import apps
    >>> Bank = apps.get_model('bank', 'Bank')
    >>> bank = Bank.get(short_name='Bank BCA')
    >>> bank.long_name
    'PT. Bank Central Asia Tbk.'
    >>> bank.short_name
    'Bank BCA'
    >>> bank.bank_code
    '014'
    >>> bank.branch_code
    '0397'
    >>> bank.bi_code
    '0140397'

Bank Field
============

``BankField`` is based on Django's ``ForeignKey``, a relationship
to Bank model.

Consider the following model using a ``BankField``:

.. code:: python

    from django.db import models
    from p1_bank.fields import BankField

    class Account(models.Model):
        name = models.CharField(max_length=100)
        bank = BankField(related_name='accounts')

Any ``Account`` instance will have a ``bank`` attribute that you can use to
identify account's bank:

.. code:: python

    >>> bank = Bank.objects.get(short_name='Bank BCA')
    >>> account = Account.objects.create(name='Kania', bank=bank)
    >>> account.bank
    'Bank BCA'
    >>> account.bank.code
    '014'
