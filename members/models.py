from django.db import models
from django.utils import timezone
from accounts.models import *
from branches.models import *

# Create your models here.
class Member(models.Model):
    #title choices
    TITLE_CHOICES = (('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'))
    #gender choices
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('None', 'None'))
    
    church = models.ForeignKey(Church, related_name='members_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branches, related_name='member_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)	
    memberid = models.CharField(max_length=100, blank=True, null=True )
    deviceid = models.CharField(max_length=100, blank=True, null=True )
    photograph = models.ImageField(upload_to = 'memberphotos', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True, choices = TITLE_CHOICES, default=None)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True, choices = GENDER_CHOICES, default=None)
    dateofbirth = models.DateField(blank = True, null=True)
    placeofbirth = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True )
    homeaddress = models.TextField(null=True, blank=True)
    postaladdress = models.TextField(null=True, blank=True)
    phonenumber1 = models.CharField(max_length=100, blank=True, null=True )
    phone1_rnotif = models.BooleanField(blank=True,  default=True)
    phonenumber2 = models.CharField(max_length=100, blank=True, null=True )
    phone2_rnotif = models.BooleanField(blank=True,  default=False)
    emailaddress1 = models.EmailField(max_length=100, blank=True, null=True)
    email1_rnotif = models.BooleanField(blank=True,  default=True)
    emailaddress2 = models.EmailField(max_length=100, blank=True, null=True)
    email2_rnotif = models.BooleanField(blank=True,  default=False)
    pushdeviceid = models.CharField(max_length=100, blank=True, null=True )
    pushdeviceid_rnotif = models.BooleanField(blank=True,  default=True)
    
    datebornagain = models.DateField(blank = True, null=True )
    datebaptised = models.DateField(blank = True, null=True )
    churchgroups = models.CharField(max_length=100, blank=True, null=True )
    ministerialposition = models.CharField(max_length=100, blank=True, null=True )
    
    convert = models.BooleanField(blank=True,  default=False)
    activestatus = models.BooleanField(blank=True,  default=True)
    deleted = models.BooleanField(blank=False,  default=False)
    datecreated = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering=('-datecreated',)

    def __str__(self):
        return self.firstname