"""
    This is the serializer for the AccessLevel model
"""
from __future__ import unicode_literals

from access.models import AccessLevel
from rest_framework import serializers


class AccessLevelSerializer(serializers.ModelSerializer):
    """
    This knows how to (de)serializer the AccessLevel model
    """
    profile = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                  view_name='profiles')
    machine = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                  view_name='machines')

    class Meta:
        model = AccessLevel
        fields = ('access_level', 'profile', 'machine',)
