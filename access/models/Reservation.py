# -*- coding: utf-8 -*-
"""Models for forge tool access control

This module contains the access control models.

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from .Machine import Machine


class Reservation(models.Model):
    """ Reservation Model

    This model represetns a Reservation.
    """
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    machine = models.ForeignKey(Machine)
    member = models.ForeignKey(User)
