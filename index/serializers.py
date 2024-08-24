from rest_framework import serializers

from index.models import EmailSubscription, Features, Testimonies

class TestimoniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonies
        exclude = ['datecreated']

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        exclude = ['datecreated']

class EmailSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        exclude = ['datecreated']