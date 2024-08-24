from rest_framework import serializers
from .models import ChurchGroup, Choices

class ChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchGroup
        exclude = ['datecreated']

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        exclude = ['datecreated']