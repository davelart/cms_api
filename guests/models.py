from django.db import models
from django.utils import timezone

from branches.models import Branches
from accounts.models import Church

class Guests(models.Model):
	# title choices
	TITLE_CHOICES = (('Mr','Mr'), ('Mrs', 'Mrs'), ('Ms','Ms'))

	# gender choices
	GENDER_CHOICES = (('Male','Male'), ('Female','Female'), ('None', 'None'))
	
	church = models.ForeignKey(Church, related_name='guest_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='guest_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
	guestid = models.CharField(max_length=100, blank=True, null=True )
	photograph = models.ImageField(upload_to = 'guestphotos', blank=True, null=True )
	title = models.CharField(('Title'), max_length=100, blank=False, null=True,  choices = TITLE_CHOICES, default = None)
	firstname = models.CharField(max_length=100, blank=True, null=True )
	middlename = models.CharField(max_length=100, blank=True, null=True )
	lastname = models.CharField(max_length=100, blank=True, null=True )
	gender = models.CharField(('Gender'), max_length=100, blank=False, null=True,  choices = GENDER_CHOICES, default = None)
	dateofbirth = models.DateField(blank = True, null=True )
	placeofbirth = models.CharField(max_length=100, blank=True, null=True )
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
	
	invitedby = models.CharField(max_length=100, blank=True, null=True )
	purposeofvisit = models.TextField(null=True, blank=True)
	deleted = models.BooleanField(blank=False,  default=False)
	
	datecreated = models.DateTimeField(default=timezone.now)
	
	def __str__(self):  
		return self.firstname