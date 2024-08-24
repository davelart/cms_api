from rest_framework import serializers
from .models import BranchReport

class BranchReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchReport
        exclude = ['datecreated']