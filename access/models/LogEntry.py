# -*- coding: utf-8 -*-
"""Models for forge tool access control

This module contains the access control models.

"""
from __future__ import unicode_literals

from django.db import models
from .Machine import Machine
from .Profile import Profile


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
    profile = models.ForeignKey(Profile, related_name='logEntries', null=False, default=0)
    machine = models.ForeignKey(Machine, related_name='logEntries', null=False)
