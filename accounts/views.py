from django.shortcuts import render
from .models import Account, Church
from django.contrib.auth.models import User
from rest_framework import generics, renderers
from .serializers import AccountSerializer, ChurchSerializer, ResetPasswordConfirmSerializer, ResetPasswordSerializer, SignInSerializer, SignUpSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
# from accounts.tasks import send_email_password_reset
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
@extend_schema_view(
    list=extend_schema(tags=["Churchs"], summary='List all Churchs'),
    create=extend_schema(tags=["Churchs"], summary='Create a Church'),
    retrieve=extend_schema(tags=["Churchs"], summary='Get a Church', examples=[]),
    update=extend_schema(tags=["Churchs"], summary='Update a Church', examples=[]),
    partial_update=extend_schema(tags=["Churchs"], summary='Patch a Church', examples=[]),
    destroy=extend_schema(tags=["Churchs"], summary='Delete a Church', examples=[]),
    # create_webhook=extend_schema(tags=["Churchs"], summary='Create Webhook', examples=[])
    )
class ChurchsViewSet(ModelViewSet):    
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'location']
    ordering_fields = ['created']
    http_method_names = ["get", "post", "put", "patch"]

@extend_schema_view(
    list=extend_schema(tags=["Accounts"], summary='List all Accounts'),
    create=extend_schema(tags=["Accounts"], summary='Create a Account'),
    retrieve=extend_schema(tags=["Accounts"], summary='Get a Account', examples=[]),
    update=extend_schema(tags=["Accounts"], summary='Update a Account', examples=[]),
    partial_update=extend_schema(tags=["Accounts"], summary='Patch a Account', examples=[]),
    destroy=extend_schema(tags=["Accounts"], summary='Delete a Account', examples=[]),
    # create_webhook=extend_schema(tags=["Accounts"], summary='Create Webhook', examples=[])
    )
class AccountsViewSet(ModelViewSet):    
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['church']
    search_fields = ['confirmed', 'onboarded']
    ordering_fields = ['created']
    http_method_names = ["get", "post", "put", "patch"]


@extend_schema_view(
    create=extend_schema(tags=["Sign In"], summary='Sign In into Account'),
    )
class SignInViewSet(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = SignInSerializer
    http_method_names = ["post"]

@extend_schema_view(
    create=extend_schema(tags=["Sign Up"], summary='Sign Up a new Church'),
    )
class SignUpViewSet(generics.CreateAPIView):
    queryset = Church.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer
    http_method_names = ["post"]


# @extend_schema_view(tags=["Reset Password"], summary='Request Password Reset')
@permission_classes([AllowAny])
class ResetPasswordViewSet(APIView):
    permission_classes = []  # Allow anyone to request a password reset

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User not found with this email address.'}, status=status.HTTP_404_NOT_FOUND)


            token = default_token_generator.make_token(user)
            # Send a password reset email to the user
            # send_email_password_reset(request=request, user=user, token=token)
            return Response({'status': 'Password reset email sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @extend_schema_view(tags=["Reset Password Confirm"], summary='Confirm Password Reset')
@permission_classes([AllowAny])
class ResetPasswordConfirmViewSet(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordConfirmSerializer(data=request.data)
        if serializer.is_valid():
            uidb64 = serializer.validated_data['uidb64']
            token = serializer.validated_data['token']
            password = serializer.validated_data['password']

            try:
                uid = urlsafe_base64_decode(uidb64)
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            if user is not None and default_token_generator.check_token(user, token):
                user.set_password(password)
                user.save()
                return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid token or user not found.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)