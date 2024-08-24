from django.shortcuts import render
from rest_framework import generics
from .models import BranchReport
from .serializers import BranchReportSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.
@extend_schema_view(
    list=extend_schema(tags=['BranchReport'], summary='List all BranchReports'),
    create=extend_schema(tags=['BranchReport'], summary='Create a BranchReport'),
    retrieve=extend_schema(tags=['BranchReport'], summary='Get a BranchReport', examples=[]),
    update=extend_schema(tags=['BranchReport'], summary='Update a BranchReport', examples=[]),
    partial_update=extend_schema(tags=['BranchReport'], summary='Patch a BranchReport', examples=[]),
    destroy=extend_schema(tags=['BranchReport'], summary='Delete a BranchReport', examples=[]),
)
class BranchReportsViewSet(ModelViewSet):
    
    serializer_class = BranchReportSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return BranchReport.objects.all()