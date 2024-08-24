from django.shortcuts import render
from rest_framework import generics
from .models import Guests
from .serializers import GuestSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Guest'], summary='List all Guests'),
    create=extend_schema(tags=['Guest'], summary='Create a Guest'),
    retrieve=extend_schema(tags=['Guest'], summary='Get a Guest', examples=[]),
    update=extend_schema(tags=['Guest'], summary='Update a Guest', examples=[]),
    partial_update=extend_schema(tags=['Guest'], summary='Patch a Guest', examples=[]),
    destroy=extend_schema(tags=['Guest'], summary='Delete a Guest', examples=[]),
)
class GuestsViewSet(ModelViewSet):
    
    serializer_class = GuestSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return Guests.objects.all()