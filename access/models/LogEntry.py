# -*- coding: utf-8 -*-
"""Models for forge tool access control

This module contains the access control models.

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from access.models import Machine


class LogEntry(models.Model):
    """ Log Entry

    This model represents a log entry.
    """
    LOG_ENTRY_TYPES = (
        ("AR", "Access Reqeust"),
        ("AG", "Access Granted"),
        ("ADL", "Access Denied Access Level"),
        ("ADR", "Access Denied Reservation"),
        ("ADM", "Access Denied Membership")
    )
    created_at = models.DateTimeField()
    entry_type = models.CharField(max_length=3, choices=LOG_ENTRY_TYPES)
    user = models.ForeignKey(User, related_name='logEntry')
    machine = models.ForeignKey('Machine')
