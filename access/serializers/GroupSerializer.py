"""
Group Serializer
"""
from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """
    This class knows how to (de)Serializer the Group model
    """

    class Meta:
        model = Group
        fields = ('url', 'name')
