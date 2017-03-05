# -*- coding: utf-8 -*-
"""Profile Model for forge tool access control

This module contains the profile model.

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from access.models import Department


class ProfileManager(models.Manager):
    def get_profile(self, member_card_id, machine_mac_address):
        pass


class Profile(models.Model):
    """ Profile Model

    Add the required fields to the User Model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_head = models.ForeignKey('Department', null=True)
    valid_membership = models.BooleanField()
    member_card_id = models.CharField(max_length=256, default="n-a")
