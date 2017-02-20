from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from access.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):

    """
    API end point that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed and edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
