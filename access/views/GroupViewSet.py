from django.contrib.auth.models import Group
from rest_framework import viewsets
from access.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed and edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
