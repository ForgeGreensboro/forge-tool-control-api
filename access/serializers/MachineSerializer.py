"""
Machine model serializer
"""

from __future__ import unicode_literals

from rest_framework import serializers

from access.models import Machine


class MachineSerializer(serializers.ModelSerializer):
    """
    Machine model (de)Serializer
    """
    department = serializers.HyperlinkedRelatedField(many=False,
                                                     read_only=True,
                                                     view_name='departments')

    class Meta:
        model = Machine
        fields = ('mac_address', 'machine_name', 'department')
