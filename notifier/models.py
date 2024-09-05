from django.db import models
from django.utils import timezone

from branches.models import Branches
from accounts.models import Church

class NotifierSettings(models.Model):
	church = models.ForeignKey(Church, related_name='notifier_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='notifier_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
	sms_sender = models.CharField(max_length=11, default='ChAffairs' )
	sms_verification = models.BooleanField(blank=True, default=False)
	sms_verification_status = models.CharField(max_length=100, blank=True, null=True, default='Unverified')
	phone_countrycode = models.CharField(max_length=255, blank=True, null=True, default='' )
	email_from = models.EmailField(max_length=255, default='branch@churchaffairs.com' )
	notifierpoints = models.BigIntegerField(null=True,  blank=True, default=0)	
	rnotif_memberadd = models.BooleanField(blank=True,  default=True)
	rnotif_guestadd = models.BooleanField(blank=True,  default=True)
	rnotif_financeadd = models.BooleanField(blank=True,  default=True)
	lastmodified = models.DateTimeField(default=timezone.now)
	
	def __str__(self):  
		return str(self.church.churchname)

class SmsSent(models.Model):
	church = models.ForeignKey(Church, related_name='smssent_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='smssent_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
	senderid = models.CharField(max_length=255, blank=True, null=True )
	message = models.TextField(max_length=255, blank=True, null=True )
	accordingto = models.CharField(max_length=255, blank=True, null=True )
	phonenumbers = models.TextField(max_length=255, blank=True, null=True )
	sentstatus = models.CharField(max_length=255, blank=True, null=True )
	datecreated = models.DateTimeField(default=timezone.now)
	
	def __str__(self):  
		return self.senderid

class EmailSent(models.Model):
	church = models.ForeignKey(Church, related_name='emailsent_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='emailsent_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)	
	subject = models.CharField(max_length=255, blank=True, null=True )
	message = models.TextField(max_length=255, blank=True, null=True )
	accordingto = models.CharField(max_length=255, blank=True, null=True )
	fromaddr = models.CharField(max_length=255, blank=True, null=True )
	toaddr = models.TextField(max_length=255, blank=True, null=True )
	sentstatus = models.CharField(max_length=255, blank=True, null=True )
	datecreated = models.DateTimeField(default=timezone.now)
	
	def __str__(self):  
		return self.subject

class PushSent(models.Model):
	church = models.ForeignKey(Church, related_name='pushnotif_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='pushnotif_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
	deviceid = models.CharField(max_length=255, blank=True, null=True )
	mediafile =  models.FileField(upload_to = 'chaffairsmedia/', blank=True, null=True)
	title = models.CharField(max_length=255, blank=True, null=True )	
	message = models.TextField(max_length=255, blank=True, null=True )
	accordingto = models.CharField(max_length=255, blank=True, null=True )
	sentstatus = models.CharField(max_length=255, blank=True, null=True )
	datecreated = models.DateTimeField(default=timezone.now)
	
	def __str__(self):  
		return self.title

class Telephony(models.Model):	
	"""This is where country codes and related things are stored, also this is used to format phonenumbers"""
	countrycode = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)
	nowithcountrycode = models.IntegerField(null=True, blank=True)
	nowithoutcountrycode = models.IntegerField(null=True, blank=True)
	supportednetworks = models.CharField(max_length=200, null=True, blank=True)
	nonetstartwith = models.IntegerField(null=True, blank=True)
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		# return self.user__memberid
		return self.countrycode