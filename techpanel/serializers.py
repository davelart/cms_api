from rest_framework import serializers

from .models import AdvancedUser, Sales, SalesUserAccount, TechChat, TechChatTicket

class AdvancedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedUser
        exclude = ['datecreated']

class SalesUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesUserAccount
        exclude = ['datecreated']

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        exclude = ['datecreated']

class TechChatTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechChatTicket
        exclude = ['datecreated']

class TechChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechChat
        exclude = ['datecreated']