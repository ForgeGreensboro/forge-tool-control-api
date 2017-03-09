"""
Access Lel view set
"""

from __future__ import unicode_literals

from rest_framework import viewsets

from access.models import AccessLevel
from access.serializers import AccessLevelSerializer


class AccessLevelViewSet(viewsets.ModelViewSet):
    """
    This is the view set for the AccessLevel model
    """

    queryset = AccessLevel.objects.all()
    serializer_class = AccessLevelSerializer
