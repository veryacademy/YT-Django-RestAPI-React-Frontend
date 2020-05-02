from rest_framework import serializers
from .models import Events


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('title', 'details')