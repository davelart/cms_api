from django.shortcuts import render
from rest_framework import generics
from .models import Branches, BranchUser
from .serializers import BranchesSerializer, BranchUserSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Branch'], summary='List all Branches'),
    create=extend_schema(tags=['Branche'], summary='Create a Branche'),
    retrieve=extend_schema(tags=['Branche'], summary='Get a Branche', examples=[]),
    update=extend_schema(tags=['Branche'], summary='Update a Branche', examples=[]),
    partial_update=extend_schema(tags=['Branche'], summary='Patch a Branche', examples=[]),
    destroy=extend_schema(tags=['Branche'], summary='Delete a Branche', examples=[]),
)
class BranchesViewSet(ModelViewSet):
    
    serializer_class = BranchesSerializer
    ordering_fields = ['datecreated']

    def get_queryset(self):
        return Branches.objects.all()

@extend_schema_view(
    list=extend_schema(tags=['BranchUser'], summary='List all BranchUsers'),
    create=extend_schema(tags=['BranchUser'], summary='Create a BranchUser'),
    retrieve=extend_schema(tags=['BranchUser'], summary='Get a BranchUser', examples=[]),
    update=extend_schema(tags=['BranchUser'], summary='Update a BranchUser', examples=[]),
    partial_update=extend_schema(tags=['BranchUser'], summary='Patch a BranchUser', examples=[]),
    destroy=extend_schema(tags=['BranchUser'], summary='Delete a BranchUser', examples=[]),
)
class BranchUserViewSet(ModelViewSet):
    
    serializer_class = BranchUserSerializer
    ordering_fields = ['datecreated']

    def get_queryset(self):
        return BranchUser.objects.all()