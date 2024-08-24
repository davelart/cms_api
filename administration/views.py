from django.shortcuts import render
from rest_framework import generics
from .models import ChurchGroup, Choices
from .serializers import ChurchGroupSerializer, ChoicesSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.
@extend_schema_view(
    list=extend_schema(tags=['ChurchGroup'], summary='List all ChurchGroups'),
    create=extend_schema(tags=['ChurchGroup'], summary='Create a ChurchGroup'),
    retrieve=extend_schema(tags=['ChurchGroup'], summary='Get a ChurchGroup', examples=[]),
    update=extend_schema(tags=['ChurchGroup'], summary='Update a ChurchGroup', examples=[]),
    partial_update=extend_schema(tags=['ChurchGroup'], summary='Patch a ChurchGroup', examples=[]),
    destroy=extend_schema(tags=['ChurchGroup'], summary='Delete a ChurchGroup', examples=[]),
)
class ChurchGroupsViewSet(ModelViewSet):
    
    serializer_class = ChurchGroupSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return ChurchGroup.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Choice'], summary='List all Choices'),
    create=extend_schema(tags=['Choice'], summary='Create a Choice'),
    retrieve=extend_schema(tags=['Choice'], summary='Get a Choice', examples=[]),
    update=extend_schema(tags=['Choice'], summary='Update a Choice', examples=[]),
    partial_update=extend_schema(tags=['Choice'], summary='Patch a Choice', examples=[]),
    destroy=extend_schema(tags=['Choice'], summary='Delete a Choice', examples=[]),
)
class ChoicesViewSet(ModelViewSet):
    
    serializer_class = ChoicesSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return Choices.objects.all()