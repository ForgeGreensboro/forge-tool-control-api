"""
LogEntry model serializer
"""
from __future__ import unicode_literals

from access.models import LogEntry
from rest_framework import serializers


class LogEntrySerializer(serializers.ModelSerializer):
    """
    This Serializer knows how to (de)serializer a LogEntry.
    """
    user = serializers.HyperlinkedRelatedField(many=False,
                                               read_only=True,
                                               view_name='users')
    machine = serializers.HyperlinkedRelatedField(many=False,
                                                  read_only=True,
                                                  view_name='machines')

    class Meta:
        model = LogEntry
        fields = ('created_at', 'entry_type', 'user', 'machine')
