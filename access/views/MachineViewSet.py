"""
Machine View Set
"""

from __future__ import unicode_literals

from rest_framework import viewsets
from access.models import Machine
from access.serializers import MachineSerializer


class MachineViewSet(viewsets.ModelViewSet):
    """
    This is hte Machine View Set
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
