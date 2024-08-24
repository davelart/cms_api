from django.shortcuts import render
from rest_framework import generics
from .models import Member
from .serializers import MemberSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.
@extend_schema_view(
    list=extend_schema(tags=['Member'], summary='List all Members'),
    create=extend_schema(tags=['Member'], summary='Create a Member'),
    retrieve=extend_schema(tags=['Member'], summary='Get a Member', examples=[]),
    update=extend_schema(tags=['Member'], summary='Update a Member', examples=[]),
    partial_update=extend_schema(tags=['Member'], summary='Patch a Member', examples=[]),
    destroy=extend_schema(tags=['Member'], summary='Delete a Member', examples=[]),
)
class MembersViewSet(ModelViewSet):
    
    serializer_class = MemberSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return Member.objects.all()