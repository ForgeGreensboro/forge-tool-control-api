"""
    Department View Set
"""
from __future__ import unicode_literals

from rest_framework import viewsets

from access.models.Department import Department
from access.serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API end point that allows Departments to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
