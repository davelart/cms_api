from rest_framework import serializers
from django.contrib.auth import get_user_model
from churchprofile.models import Account, Register, ChurchProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'is_staff']

class AccountProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ['user', 'photograph', 'gender', 'phone', 'confirmed', 'identifier',]

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        exclude = ['datecreated']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchProfile
        exclude = ['datecreated']