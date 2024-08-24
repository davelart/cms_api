from rest_framework import serializers

from notifier.models import EmailSent, NotifierSettings, PushSent, SmsSent, Telephony

class NotifierSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotifierSettings
        fields = '__all__'

class SmsSentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsSent
        exclude = ['datecreated']

class EmailSentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSent
        exclude = ['datecreated']

class PushSentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushSent
        exclude = ['datecreated']
        
class TelephonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephony
        exclude = ['datecreated']