# -*- coding: utf-8 -*-
"""Models for forge tool access control

This module contains the access control models.

"""
from __future__ import unicode_literals

from django.db import models

from .Profile import Profile
from .Machine import  Machine


class AccessLevel(models.Model):
    """ Access Level for each machine.

    This Model represents the Access Level required for each
    machine.
    """
    ACCESS_LEVEL_CHOICES = (
        ('FULL', 'Full access to Machine'),
        ('SUPER', 'Supervised Access to the Machine'),
        ('NONE', 'No Access to the Machine'),
    )
    access_level = models.CharField(max_length=10, default="NONE")
    profile = models.ForeignKey(Profile, null=True)
    machine = models.ForeignKey(Machine, null=True, blank=True)
