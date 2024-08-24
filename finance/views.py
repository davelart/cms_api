from django.shortcuts import render
from rest_framework import generics
from .models import AccountExpenditure, AccountPayment, AccountSetup
from .serializers import AccountExpenditureSerializer, AccountPaymentSerializer, AccountSetupSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['AccountSetup'], summary='List all AccountSetups'),
    create=extend_schema(tags=['AccountSetup'], summary='Create a AccountSetup'),
    retrieve=extend_schema(tags=['AccountSetup'], summary='Get a AccountSetup', examples=[]),
    update=extend_schema(tags=['AccountSetup'], summary='Update a AccountSetup', examples=[]),
    partial_update=extend_schema(tags=['AccountSetup'], summary='Patch a AccountSetup', examples=[]),
    destroy=extend_schema(tags=['AccountSetup'], summary='Delete a AccountSetup', examples=[]),
)
class AccountSetupViewSet(ModelViewSet):
    
    serializer_class = AccountSetupSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AccountSetup.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['AccountPayment'], summary='List all AccountPayments'),
    create=extend_schema(tags=['AccountPayment'], summary='Create a AccountPayment'),
    retrieve=extend_schema(tags=['AccountPayment'], summary='Get a AccountPayment', examples=[]),
    update=extend_schema(tags=['AccountPayment'], summary='Update a AccountPayment', examples=[]),
    partial_update=extend_schema(tags=['AccountPayment'], summary='Patch a AccountPayment', examples=[]),
    destroy=extend_schema(tags=['AccountPayment'], summary='Delete a AccountPayment', examples=[]),
)
class AccountPaymentViewSet(ModelViewSet):
    
    serializer_class = AccountPaymentSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AccountPayment.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['AccountExpenditure'], summary='List all AccountExpenditures'),
    create=extend_schema(tags=['AccountExpenditure'], summary='Create a AccountExpenditure'),
    retrieve=extend_schema(tags=['AccountExpenditure'], summary='Get a AccountExpenditure', examples=[]),
    update=extend_schema(tags=['AccountExpenditure'], summary='Update a AccountExpenditure', examples=[]),
    partial_update=extend_schema(tags=['AccountExpenditure'], summary='Patch a AccountExpenditure', examples=[]),
    destroy=extend_schema(tags=['AccountExpenditure'], summary='Delete a AccountExpenditure', examples=[]),
)
class AccountExpenditureViewSet(ModelViewSet):
    
    serializer_class = AccountExpenditureSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AccountExpenditure.objects.all()