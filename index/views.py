from django.shortcuts import render
from rest_framework import generics
from .models import EmailSubscription, Features, Testimonies
from .serializers import FeaturesSerializer, TestimoniesSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Testimony'], summary='List all Testimonies'),
    create=extend_schema(tags=['Testimony'], summary='Create a Testimony'),
    retrieve=extend_schema(tags=['Testimony'], summary='Get a Testimony', examples=[]),
    update=extend_schema(tags=['Testimony'], summary='Update a Testimony', examples=[]),
    partial_update=extend_schema(tags=['Testimony'], summary='Patch a Testimony', examples=[]),
    destroy=extend_schema(tags=['Testimony'], summary='Delete a Testimony', examples=[]),
)
class TestimoniesViewSet(ModelViewSet):
    
    serializer_class = TestimoniesSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return Testimonies.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Feature'], summary='List all Features'),
    create=extend_schema(tags=['Feature'], summary='Create a Feature'),
    retrieve=extend_schema(tags=['Feature'], summary='Get a Feature', examples=[]),
    update=extend_schema(tags=['Feature'], summary='Update a Feature', examples=[]),
    partial_update=extend_schema(tags=['Feature'], summary='Patch a Feature', examples=[]),
    destroy=extend_schema(tags=['Feature'], summary='Delete a Feature', examples=[]),
)
class FeaturesViewSet(ModelViewSet):
    
    serializer_class = FeaturesSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return Features.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Email Subscription'], summary='List all Email Subscriptions'),
    create=extend_schema(tags=['Email Subscription'], summary='Create a Email Subscription'),
    retrieve=extend_schema(tags=['Email Subscription'], summary='Get a Email Subscription', examples=[]),
    update=extend_schema(tags=['Email Subscription'], summary='Update a Email Subscription', examples=[]),
    partial_update=extend_schema(tags=['Email Subscription'], summary='Patch a Email Subscription', examples=[]),
    destroy=extend_schema(tags=['Email Subscription'], summary='Delete a Email Subscription', examples=[]),
)
class EmailSubscriptionsViewSet(ModelViewSet):
    
    serializer_class = TestimoniesSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return EmailSubscription.objects.all()