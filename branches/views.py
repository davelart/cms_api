from django.shortcuts import render
from rest_framework import generics
from .models import Branches, BranchUser
from .serializers import BranchesSerializer, BranchUserSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Branch'], summary='List all Branches'),
    create=extend_schema(tags=['Branch'], summary='Create a Branch'),
    retrieve=extend_schema(tags=['Branch'], summary='Get a Branch', examples=[]),
    update=extend_schema(tags=['Branch'], summary='Update a Branch', examples=[]),
    partial_update=extend_schema(tags=['Branch'], summary='Patch a Branch', examples=[]),
    destroy=extend_schema(tags=['Branch'], summary='Delete a Branch', examples=[]),
)
class BranchesViewSet(ModelViewSet):
    
    serializer_class = BranchesSerializer
    ordering_fields = ['datecreated']

    def get_queryset(self):
        return Branches.objects.all()

@extend_schema_view(
    list=extend_schema(tags=['Branch User'], summary='List all Branch Users'),
    create=extend_schema(tags=['Branch User'], summary='Create a Branch User'),
    retrieve=extend_schema(tags=['Branch User'], summary='Get a Branch User', examples=[]),
    update=extend_schema(tags=['Branch User'], summary='Update a Branch User', examples=[]),
    partial_update=extend_schema(tags=['Branch User'], summary='Patch a Branch User', examples=[]),
    destroy=extend_schema(tags=['Branch User'], summary='Delete a Branch User', examples=[]),
)
class BranchUserViewSet(ModelViewSet):
    
    serializer_class = BranchUserSerializer
    ordering_fields = ['datecreated']

    def get_queryset(self):
        return BranchUser.objects.all()