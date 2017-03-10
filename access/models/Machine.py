# -*- coding: utf-8 -*-
"""Models for forge tool access control

This module contains the access control models.

"""
from __future__ import unicode_literals

from django.db import models

from .Department import Department


class Machine(models.Model):
    """ Machine Model.

        This Model represents a machine in the system.
    """
    mac_address = models.CharField(max_length=15)
    machine_name = models.CharField(max_length=128)
    department = models.ForeignKey(Department)
