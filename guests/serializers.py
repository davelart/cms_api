from rest_framework import serializers

from guests.models import Guests

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        exclude = ['datecreated']