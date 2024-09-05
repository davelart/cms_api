from django.shortcuts import render
from rest_framework import generics
from .models import AccountExpenditure, AccountPayment, AccountSetup
from .serializers import AccountExpenditureSerializer, AccountPaymentSerializer, AccountSetupSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Account Setup'], summary='List all Account Setups'),
    create=extend_schema(tags=['Account Setup'], summary='Create a Account Setup'),
    retrieve=extend_schema(tags=['Account Setup'], summary='Get a Account Setup', examples=[]),
    update=extend_schema(tags=['Account Setup'], summary='Update a Account Setup', examples=[]),
    partial_update=extend_schema(tags=['Account Setup'], summary='Patch a Account Setup', examples=[]),
    destroy=extend_schema(tags=['Account Setup'], summary='Delete a Account Setup', examples=[]),
)
class AccountSetupViewSet(ModelViewSet):
    
    serializer_class = AccountSetupSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AccountSetup.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Account Payment'], summary='List all Account Payments'),
    create=extend_schema(tags=['Account Payment'], summary='Create a Account Payment'),
    retrieve=extend_schema(tags=['Account Payment'], summary='Get a Account Payment', examples=[]),
    update=extend_schema(tags=['Account Payment'], summary='Update a Account Payment', examples=[]),
    partial_update=extend_schema(tags=['Account Payment'], summary='Patch a Account Payment', examples=[]),
    destroy=extend_schema(tags=['Account Payment'], summary='Delete a Account Payment', examples=[]),
)
class AccountPaymentViewSet(ModelViewSet):
    
    serializer_class = AccountPaymentSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AccountPayment.objects.all()
    
@extend_schema_view(
    list=extend_schema(tags=['Account Expenditure'], summary='List all Account Expenditures'),
    create=extend_schema(tags=['Account Expenditure'], summary='Create a Account Expenditure'),
    retrieve=extend_schema(tags=['Account Expenditure'], summary='Get a Account Expenditure', examples=[]),
    update=extend_schema(tags=['Account Expenditure'], summary='Update a Account Expenditure', examples=[]),
    partial_update=extend_schema(tags=['Account Expenditure'], summary='Patch a Account Expenditure', examples=[]),
    destroy=extend_schema(tags=['Account Expenditure'], summary='Delete a Account Expenditure', examples=[]),
)
class AccountExpenditureViewSet(ModelViewSet):
    
    serializer_class = AccountExpenditureSerializer
    ordering_fields = ['datecreated']
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        return AccountExpenditure.objects.all()