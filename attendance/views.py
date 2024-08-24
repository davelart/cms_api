from django.shortcuts import render
from rest_framework import generics
from .models import Attendance, AttendanceProgram
from .serializers import AttendanceProgramSerializer, AttendanceSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(tags=['AttendanceProgram'], summary='List all AttendanceProgram'),
    create=extend_schema(tags=['AttendanceProgram'], summary='Create a AttendanceProgram'),
    retrieve=extend_schema(tags=['AttendanceProgram'], summary='Get a AttendanceProgram', examples=[]),
    update=extend_schema(tags=['AttendanceProgram'], summary='Update a AttendanceProgram', examples=[]),
    partial_update=extend_schema(tags=['AttendanceProgram'], summary='Patch a AttendanceProgram', examples=[]),
    destroy=extend_schema(tags=['AttendanceProgram'], summary='Delete a AttendanceProgram', examples=[]),
)
class AttendanceProgramsViewSet(ModelViewSet):
    
    serializer_class = AttendanceProgramSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AttendanceProgram.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Attendance'], summary='List all Attendance'),
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