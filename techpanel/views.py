from django.shortcuts import render
from rest_framework import generics
from .models import AdvancedUser, Sales, SalesUserAccount, TechChat, TechChatTicket
from .serializers import AdvancedUserSerializer, SalesSerializer, SalesUserAccountSerializer, TechChatSerializer, TechChatTicketSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['AdvancedUser'], summary='List all AdvancedUsers'),
    create=extend_schema(tags=['AdvancedUser'], summary='Create a AdvancedUser'),
    retrieve=extend_schema(tags=['AdvancedUser'], summary='Get a AdvancedUser', examples=[]),
    update=extend_schema(tags=['AdvancedUser'], summary='Update a AdvancedUser', examples=[]),
    partial_update=extend_schema(tags=['AdvancedUser'], summary='Patch a AdvancedUser', examples=[]),
    destroy=extend_schema(tags=['AdvancedUser'], summary='Delete a AdvancedUser', examples=[]),
)
class AdvancedUsersViewSet(ModelViewSet):
    
    serializer_class = AdvancedUserSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AdvancedUser.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['SalesUserAccount'], summary='List all SalesUserAccounts'),
    create=extend_schema(tags=['SalesUserAccount'], summary='Create a SalesUserAccount'),
    retrieve=extend_schema(tags=['SalesUserAccount'], summary='Get a SalesUserAccount', examples=[]),
    update=extend_schema(tags=['SalesUserAccount'], summary='Update a SalesUserAccount', examples=[]),
    partial_update=extend_schema(tags=['SalesUserAccount'], summary='Patch a SalesUserAccount', examples=[]),
    destroy=extend_schema(tags=['SalesUserAccount'], summary='Delete a SalesUserAccount', examples=[]),
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
    list=extend_schema(tags=['TechChatTicket'], summary='List all TechChatTickets'),
    create=extend_schema(tags=['TechChatTicket'], summary='Create a TechChatTicket'),
    retrieve=extend_schema(tags=['TechChatTicket'], summary='Get a TechChatTicket', examples=[]),
    update=extend_schema(tags=['TechChatTicket'], summary='Update a TechChatTicket', examples=[]),
    partial_update=extend_schema(tags=['TechChatTicket'], summary='Patch a TechChatTicket', examples=[]),
    destroy=extend_schema(tags=['TechChatTicket'], summary='Delete a TechChatTicket', examples=[]),
)
class TechChatTicketsViewSet(ModelViewSet):
    
    serializer_class = TechChatTicketSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return TechChatTicket.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['TechChat'], summary='List all TechChats'),
    create=extend_schema(tags=['TechChat'], summary='Create a TechChat'),
    retrieve=extend_schema(tags=['TechChat'], summary='Get a TechChat', examples=[]),
    update=extend_schema(tags=['TechChat'], summary='Update a TechChat', examples=[]),
    partial_update=extend_schema(tags=['TechChat'], summary='Patch a TechChat', examples=[]),
    destroy=extend_schema(tags=['TechChat'], summary='Delete a TechChat', examples=[]),
)
class TechChatsViewSet(ModelViewSet):
    
    serializer_class = TechChatSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return TechChat.objects.all()