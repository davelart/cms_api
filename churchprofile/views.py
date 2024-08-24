from django.shortcuts import render
from rest_framework import generics
from .models import Register, ChurchProfile
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Register'], summary='List all Registers'),
    create=extend_schema(tags=['Register'], summary='Create a Register'),
    retrieve=extend_schema(tags=['Register'], summary='Get a Register', examples=[]),
    update=extend_schema(tags=['Register'], summary='Update a Register', examples=[]),
    partial_update=extend_schema(tags=['Register'], summary='Patch a Register', examples=[]),
    destroy=extend_schema(tags=['Register'], summary='Delete a Register', examples=[]),
)
class RegisterViewSet(ModelViewSet):
    
    serializer_class = RegisterSerializer
    ordering_fields = ['datecreated']

    def get_queryset(self):
        return Register.objects.all()

@extend_schema_view(
    list=extend_schema(tags=['Profile'], summary='List all Profiles'),
    create=extend_schema(tags=['Profile'], summary='Create a Profile'),
    retrieve=extend_schema(tags=['Profile'], summary='Get a Profile', examples=[]),
    update=extend_schema(tags=['Profile'], summary='Update a Profile', examples=[]),
    partial_update=extend_schema(tags=['Profile'], summary='Patch a Profile', examples=[]),
    destroy=extend_schema(tags=['Profile'], summary='Delete a Profile', examples=[]),
)
class ProfileViewSet(ModelViewSet):
    
    serializer_class = ProfileSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return ChurchProfile.objects.all()