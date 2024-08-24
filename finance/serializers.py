from rest_framework import serializers
from .models import AccountExpenditure, AccountPayment, AccountSetup

class AccountSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSetup
        exclude = ['datecreated']

class AccountPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountPayment
        exclude = ['datecreated']

class AccountExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountExpenditure
        exclude = ['datecreated']