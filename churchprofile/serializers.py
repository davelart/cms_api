from rest_framework import serializers
from .models import Register, ChurchProfile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        exclude = ['datecreated']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchProfile
        exclude = ['datecreated']