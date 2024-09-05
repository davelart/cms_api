from django.shortcuts import render
from rest_framework import generics
from .models import EmailSent, NotifierSettings, PushSent, SmsSent, Telephony
from .serializers import EmailSentSerializer, NotifierSettingsSerializer, PushSentSerializer, SmsSentSerializer, TelephonySerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Notifier Setting'], summary='List all Notifier Settings'),
    create=extend_schema(tags=['Notifier Setting'], summary='Create a Notifier Setting'),
    retrieve=extend_schema(tags=['Notifier Setting'], summary='Get a Notifier Setting', examples=[]),
    update=extend_schema(tags=['Notifier Setting'], summary='Update a Notifier Setting', examples=[]),
    partial_update=extend_schema(tags=['Notifier Setting'], summary='Patch a Notifier Setting', examples=[]),
    destroy=extend_schema(tags=['Notifier Setting'], summary='Delete a Notifier Setting', examples=[]),
)
class NotifierSettingssViewSet(ModelViewSet):
    serializer_class = NotifierSettingsSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return NotifierSettings.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Sent Sms'], summary='List all Sent Sms'),
    create=extend_schema(tags=['Sent Sms'], summary='Create a Sent Sms'),
    retrieve=extend_schema(tags=['Sent Sms'], summary='Get a Sent Sms', examples=[]),
    update=extend_schema(tags=['Sent Sms'], summary='Update a Sent Sms', examples=[]),
    partial_update=extend_schema(tags=['Sent Sms'], summary='Patch a Sent Sms', examples=[]),
    destroy=extend_schema(tags=['Sent Sms'], summary='Delete a Sent Sms', examples=[]),
)
class SmsSentsViewSet(ModelViewSet):
    serializer_class = SmsSentSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return SmsSent.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Sent Email'], summary='List all Sent Emails'),
    create=extend_schema(tags=['Sent Email'], summary='Create a Sent Email'),
    retrieve=extend_schema(tags=['Sent Email'], summary='Get a Sent Email', examples=[]),
    update=extend_schema(tags=['Sent Email'], summary='Update a Sent Email', examples=[]),
    partial_update=extend_schema(tags=['Sent Email'], summary='Patch a Sent Email', examples=[]),
    destroy=extend_schema(tags=['Sent Email'], summary='Delete a Sent Email', examples=[]),
)
class EmailSentsViewSet(ModelViewSet):
    serializer_class = EmailSentSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return EmailSent.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Sent Push'], summary='List all Sent Pushs'),
    create=extend_schema(tags=['Sent Push'], summary='Create a Sent Push'),
    retrieve=extend_schema(tags=['Sent Push'], summary='Get a Sent Push', examples=[]),
    update=extend_schema(tags=['Sent Push'], summary='Update a Sent Push', examples=[]),
    partial_update=extend_schema(tags=['Sent Push'], summary='Patch a Sent Push', examples=[]),
    destroy=extend_schema(tags=['Sent Push'], summary='Delete a Sent Push', examples=[]),
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