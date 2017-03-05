# -*- coding: utf-8 -*-
"""Department Model for forge tool access control

This module contains the Department model.

"""
from __future__ import unicode_literals

from django.db import models

class DepartmentManager(models.Manager):
    def get_by_department(self, department):
        self.filter(department=department)


class Department(models.Model):
    """ Department for each machine

    This model represents the Department that each machinea
    is located in.
    """
    objects = DepartmentManager()
    name = models.CharField(max_length=50)
