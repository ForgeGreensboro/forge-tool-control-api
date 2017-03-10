"""
LogEntryViewSet
"""

from __future__ import unicode_literals

from rest_framework import viewsets
from access.serializers import LogEntrySerializer
from access.models import LogEntry


class LogEntryViewSet(viewsets.ModelViewSet):
    """
    This is the view for the Log Entry
    """
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
