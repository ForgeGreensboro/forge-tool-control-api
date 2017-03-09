"""
This Contains the Department Serializer
"""
from __future__ import unicode_literals

from access.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    This serializer knows how to (de)serialize the Department Model
    """
    class Meta:
        model = Department
        fields = ('name')
