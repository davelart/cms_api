from rest_framework import serializers
from .models import Branches, BranchUser

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        exclude = ['datecreated']

class BranchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchUser
        exclude = ['datecreated']