from django.shortcuts import render
from rest_framework import generics
from .models import BranchReport
from .serializers import BranchReportSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.
@extend_schema_view(
    list=extend_schema(tags=['Branch Report'], summary='List all Branch Reports'),
    create=extend_schema(tags=['Branch Report'], summary='Create a Branch Report'),
    retrieve=extend_schema(tags=['Branch Report'], summary='Get a Branch Report', examples=[]),
    update=extend_schema(tags=['Branch Report'], summary='Update a Branch Report', examples=[]),
    partial_update=extend_schema(tags=['Branch Report'], summary='Patch a Branch Report', examples=[]),
    destroy=extend_schema(tags=['Branch Report'], summary='Delete a Branch Report', examples=[]),
)
class BranchReportsViewSet(ModelViewSet):
    
    serializer_class = BranchReportSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return BranchReport.objects.all()