from django.shortcuts import render
from rest_framework import generics
from .models import AdvancedUser, Sales, SalesUserAccount, TechChat, TechChatTicket
from .serializers import AdvancedUserSerializer, SalesSerializer, SalesUserAccountSerializer, TechChatSerializer, TechChatTicketSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Advanced User'], summary='List all Advanced Users'),
    create=extend_schema(tags=['Advanced User'], summary='Create a Advanced User'),
    retrieve=extend_schema(tags=['Advanced User'], summary='Get a Advanced User', examples=[]),
    update=extend_schema(tags=['Advanced User'], summary='Update a Advanced User', examples=[]),
    partial_update=extend_schema(tags=['Advanced User'], summary='Patch a Advanced User', examples=[]),
    destroy=extend_schema(tags=['Advanced User'], summary='Delete a Advanced User', examples=[]),
)
class AdvancedUsersViewSet(ModelViewSet):
    
    serializer_class = AdvancedUserSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AdvancedUser.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Sales User Account'], summary='List all Sales User Accounts'),
    create=extend_schema(tags=['Sales User Account'], summary='Create a Sales User Account'),
    retrieve=extend_schema(tags=['Sales User Account'], summary='Get a Sales User Account', examples=[]),
    update=extend_schema(tags=['Sales User Account'], summary='Update a Sales User Account', examples=[]),
    partial_update=extend_schema(tags=['Sales User Account'], summary='Patch a Sales User Account', examples=[]),
    destroy=extend_schema(tags=['Sales User Account'], summary='Delete a Sales User Account', examples=[]),
)
class SalesUserAccountsViewSet(ModelViewSet):
    
    serializer_class = SalesUserAccountSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return SalesUserAccount.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Sales'], summary='List all Sales'),
    create=extend_schema(tags=['Sales'], summary='Create a Sales'),
    retrieve=extend_schema(tags=['Sales'], summary='Get a Sales', examples=[]),
    update=extend_schema(tags=['Sales'], summary='Update a Sales', examples=[]),
    partial_update=extend_schema(tags=['Sales'], summary='Patch a Sales', examples=[]),
    destroy=extend_schema(tags=['Sales'], summary='Delete a Sales', examples=[]),
)
class SalesViewSet(ModelViewSet):
    
    serializer_class = SalesSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return Sales.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Tech Chat Ticket'], summary='List all Tech Chat Tickets'),
    create=extend_schema(tags=['Tech Chat Ticket'], summary='Create a Tech Chat Ticket'),
    retrieve=extend_schema(tags=['Tech Chat Ticket'], summary='Get a Tech Chat Ticket', examples=[]),
    update=extend_schema(tags=['Tech Chat Ticket'], summary='Update a Tech Chat Ticket', examples=[]),
    partial_update=extend_schema(tags=['Tech Chat Ticket'], summary='Patch a Tech Chat Ticket', examples=[]),
    destroy=extend_schema(tags=['Tech Chat Ticket'], summary='Delete a Tech Chat Ticket', examples=[]),
)
class TechChatTicketsViewSet(ModelViewSet):
    
    serializer_class = TechChatTicketSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return TechChatTicket.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Tech Chat'], summary='List all Tech Chats'),
    create=extend_schema(tags=['Tech Chat'], summary='Create a Tech Chat'),
    retrieve=extend_schema(tags=['Tech Chat'], summary='Get a Tech Chat', examples=[]),
    update=extend_schema(tags=['Tech Chat'], summary='Update a Tech Chat', examples=[]),
    partial_update=extend_schema(tags=['Tech Chat'], summary='Patch a Tech Chat', examples=[]),
    destroy=extend_schema(tags=['Tech Chat'], summary='Delete a Tech Chat', examples=[]),
)
class TechChatsViewSet(ModelViewSet):
    
    serializer_class = TechChatSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return TechChat.objects.all()