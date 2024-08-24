from django.shortcuts import render
from rest_framework import generics
from .models import EmailSent, NotifierSettings, PushSent, SmsSent, Telephony
from .serializers import EmailSentSerializer, NotifierSettingsSerializer, PushSentSerializer, SmsSentSerializer, TelephonySerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['NotifierSetting'], summary='List all NotifierSettings'),
    create=extend_schema(tags=['NotifierSetting'], summary='Create a NotifierSetting'),
    retrieve=extend_schema(tags=['NotifierSetting'], summary='Get a NotifierSetting', examples=[]),
    update=extend_schema(tags=['NotifierSetting'], summary='Update a NotifierSetting', examples=[]),
    partial_update=extend_schema(tags=['NotifierSetting'], summary='Patch a NotifierSetting', examples=[]),
    destroy=extend_schema(tags=['NotifierSetting'], summary='Delete a NotifierSetting', examples=[]),
)
class NotifierSettingssViewSet(ModelViewSet):
    serializer_class = NotifierSettingsSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return NotifierSettings.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['SmsSent'], summary='List all SmsSents'),
    create=extend_schema(tags=['SmsSent'], summary='Create a SmsSent'),
    retrieve=extend_schema(tags=['SmsSent'], summary='Get a SmsSent', examples=[]),
    update=extend_schema(tags=['SmsSent'], summary='Update a SmsSent', examples=[]),
    partial_update=extend_schema(tags=['SmsSent'], summary='Patch a SmsSent', examples=[]),
    destroy=extend_schema(tags=['SmsSent'], summary='Delete a SmsSent', examples=[]),
)
class SmsSentsViewSet(ModelViewSet):
    serializer_class = SmsSentSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return SmsSent.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Emailsent'], summary='List all Emailsents'),
    create=extend_schema(tags=['Emailsent'], summary='Create a Emailsent'),
    retrieve=extend_schema(tags=['Emailsent'], summary='Get a Emailsent', examples=[]),
    update=extend_schema(tags=['Emailsent'], summary='Update a Emailsent', examples=[]),
    partial_update=extend_schema(tags=['Emailsent'], summary='Patch a Emailsent', examples=[]),
    destroy=extend_schema(tags=['Emailsent'], summary='Delete a Emailsent', examples=[]),
)
class EmailSentsViewSet(ModelViewSet):
    serializer_class = EmailSentSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return EmailSent.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['PushSent'], summary='List all PushSents'),
    create=extend_schema(tags=['PushSent'], summary='Create a PushSent'),
    retrieve=extend_schema(tags=['PushSent'], summary='Get a PushSent', examples=[]),
    update=extend_schema(tags=['PushSent'], summary='Update a PushSent', examples=[]),
    partial_update=extend_schema(tags=['PushSent'], summary='Patch a PushSent', examples=[]),
    destroy=extend_schema(tags=['PushSent'], summary='Delete a PushSent', examples=[]),
)
class PushSentsViewSet(ModelViewSet):
    serializer_class = PushSentSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return PushSent.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Telephony'], summary='List all Telephonies'),
    create=extend_schema(tags=['Telephony'], summary='Create a Telephony'),
    retrieve=extend_schema(tags=['Telephony'], summary='Get a Telephony', examples=[]),
    update=extend_schema(tags=['Telephony'], summary='Update a Telephony', examples=[]),
    partial_update=extend_schema(tags=['Telephony'], summary='Patch a Telephony', examples=[]),
    destroy=extend_schema(tags=['Telephony'], summary='Delete a Telephony', examples=[]),
)
class TelephonyViewSet(ModelViewSet):
    serializer_class = TelephonySerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return Telephony.objects.all()