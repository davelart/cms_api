from members.models import Member
from .models import Account, Church
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()

class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        exclude = ['created']

class AccountSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    middle_name = serializers.CharField(source='user.middle_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Account
        fields = '__all__'

class SignInSerializer(TokenObtainPairSerializer):
  
  def validate(self, attrs):
        data = super().validate(attrs)
        try:            
          try:
              account = Account.objects.get(user=self.user)
          except Account.DoesNotExist:
            account = None
            
          members = Member.objects.filter(church=account.church)
            
          data['first_name'] = self.user.first_name if self.user is not None else ''
          data['last_name'] = self.user.last_name if self.user is not None else ''
          data['email'] = self.user.email if self.user is not None else ''
          
        #   data['staff_identifier'] = staff.identifier if staff is not None else ''
            
          data['role'] = 'Administrator'
          data['confirmed'] = account.confirmed if account is not None else ''
          # data['onboarded'] = account.onboarded if account is not None else ''
          
          data['church'] = {
            "identifier":account.church.identifier if account.church is not None else '',
            "name":account.church.name if account.church is not None else '',
            "phone":account.church.phone if account.church is not None else '',
            "email":account.church.email if account.church is not None else '',
            "address":account.church.address if account.church is not None else '',
            "logo":account.church.logo if account.church is not None else '',
            "payment_plan":account.church.payment_plan if account.church is not None else '',
            "next_expiry_date":account.church.next_expiry_date if account.church is not None else '',
            "members_count":members.count() if members is not None else 0
          }
          
        except Exception as e:
          return f'Error {e}'
        
        return data

  @classmethod
  def get_token(cls, user):
      # token = super(SignInSerializer, cls).get_token(user)
      token = super().get_token(user)

      return token

class SignUpSerializer(serializers.ModelSerializer):
  class Meta:
    model = Church
    fields = ('name', 'first_name', 'last_name', 'phone', 'email', 'password', 'confirm_password', 'username' )
    extra_kwargs = {
      'name': {'required': True},
      'first_name': {'required': True},
      'last_name': {'required': True},
      'phone': {'required': True},
      'email': {'required': True},
      'username': {'required': True},
      # 'date_of_birth': {'required': True},
      'password': {'required': True},
      'confirm_password': {'required': True},
      # 'country': {'required': True},
      # 'payment_plan': {'required': True}
    }
  def validate(self, attrs):
    try:
      user_exist =  User.objects.get(username=attrs['username'])
      raise serializers.ValidationError({"username": "Username already Exists"})
    except User.DoesNotExist:
      pass
    
    if attrs['password'] != attrs['confirm_password']:
      raise serializers.ValidationError({"password": "Password fields didn't match."})
    
    
    return attrs
  def create(self, validated_data):
    church = Church.objects.create(
        name=validated_data['name'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        phone=validated_data['phone'],
        email=validated_data['email'],
        username=validated_data['username'],
        # date_of_birth=validated_data['date_of_birth'],
        password=validated_data['password'],
        confirm_password=validated_data['confirm_password'],
        # country=validated_data['country'],
        # payment_plan=validated_data['payment_plan']
        )
    return church
  
class ResetPasswordSerializer(serializers.Serializer):    
  email = serializers.EmailField(required=True)
    
  def validate_email(self, value):
        user = User.objects.filter(email=value).first()
        if user is None:
            raise serializers.ValidationError('User with this email address does not exist')
        return value
      
class ResetPasswordConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        uidb64 = data['uidb64']
        token = data['token']
        password = data['password']

        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError({'error': 'Invalid uidb64 or user not found.'})

        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError({'error': 'Invalid token.'})

        data['user'] = user
        return data