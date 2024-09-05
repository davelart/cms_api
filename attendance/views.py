from django.shortcuts import render
from rest_framework import generics
from .models import Attendance, AttendanceProgram
from .serializers import AttendanceProgramSerializer, AttendanceSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(tags=['Attendance Program'], summary='List all Attendance Program'),
    create=extend_schema(tags=['Attendance Program'], summary='Create a Attendance Program'),
    retrieve=extend_schema(tags=['Attendance Program'], summary='Get a Attendance Program', examples=[]),
    update=extend_schema(tags=['Attendance Program'], summary='Update a Attendance Program', examples=[]),
    partial_update=extend_schema(tags=['Attendance Program'], summary='Patch a Attendance Program', examples=[]),
    destroy=extend_schema(tags=['Attendance Program'], summary='Delete a Attendance Program', examples=[]),
)
class AttendanceProgramsViewSet(ModelViewSet):
    
    serializer_class = AttendanceProgramSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AttendanceProgram.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Attendance'], summary='List all Attendances'),
    create=extend_schema(tags=['Attendance'], summary='Create a Attendance'),
    retrieve=extend_schema(tags=['Attendance'], summary='Get a Attendance', examples=[]),
    update=extend_schema(tags=['Attendance'], summary='Update a Attendance', examples=[]),
    partial_update=extend_schema(tags=['Attendance'], summary='Patch a Attendance', examples=[]),
    destroy=extend_schema(tags=['Attendance'], summary='Delete a Attendance', examples=[]),
)
class AttendancesViewSet(ModelViewSet):

    serializer_class = AttendanceSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return Attendance.objects.all()