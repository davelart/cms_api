from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
# from django_countries.fields import CountryField

# Create your models here.
class Church(models.Model):
    class PaymentPlan(models.TextChoices):
        FREE = 'Free', 'Free'
        BASIC = 'Basic', 'Basic'
        GOLD = 'Gold', 'Gold'
        DIAMOND = 'Diamond', 'Diamond'
    
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    logo = models.URLField(blank=True, null=True)
    motto = models.CharField(max_length=100, null=True, blank=True, default='')
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100, null=True, blank=True, default='')
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True, default='')
    confirm_password = models.CharField(max_length=100, null=True, blank=True, default='')
    address = models.TextField(max_length=1000, null=True, blank=True, default='')
    postal = models.TextField(max_length=1000, null=True, blank=True, default='')
    bank_name = models.CharField(max_length=100, blank=True, null=True, default='')
    bank_account_number = models.CharField(max_length=100, blank=True, null=True, default='')
    # country = CountryField(default='GH')
    active = models.BooleanField(blank=False, default=True)
    payment_plan = models.CharField(max_length=255, null=True, choices=PaymentPlan.choices, default=PaymentPlan.BASIC)
    next_expiry_date = models.DateField(blank=True, null=True, default=timezone.now)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class Account(models.Model):   
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE, default=1)
    church = models.ForeignKey(Church, related_name="account_church", null=False, on_delete=models.CASCADE)    
    photo = models.URLField(blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user}"