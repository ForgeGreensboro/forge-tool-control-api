# -*- coding: utf-8 -*-
"""Models for forge tool access control

This module contains the access control models.

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    """ Department for each machine

    This model represents the Department that each machine
    is located in.
    """
    name = models.CharField(max_length=50)


class Profile(models.Model):
    """ Profile Model

    Add the required fields to the User Model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_head = models.ForeignKey(Department, null=True)
    valid_membership = models.BooleanField()


class AccessLevel(models.Model):
    """ Access Level for each machine.

    This Model represents the Access Level required for each
    machine.
    """
    access_level = models.CharField(max_length=50)


class Machine(models.Model):
    """ Machine Model.

        This Model represents a machine in the system.
    """
    mac_address = models.CharField(max_length=15)
    machine_name = models.CharField(max_length=50)
    access_level = models.ForeignKey(AccessLevel)
    department = models.ForeignKey(Department)


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
    machine = models.ForeignKey(Machine)


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
