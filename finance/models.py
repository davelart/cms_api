from django.db import models
from django.utils import timezone

from branches.models import Branches
from churchprofile.models import ChurchProfile

class AccountSetup(models.Model):	
    church = models.ForeignKey(ChurchProfile, related_name='accountsetup_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branches, related_name='accountsetup_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
    accountname = models.CharField(max_length=255, blank=True, null=True, default='')
    accounttype = models.CharField(max_length=255, blank=True, null=True, default='')
    purpose = models.TextField(blank=True, null=True, default='')
    deleted = models.BooleanField(blank=False,  default=False)
    datecreated = models.DateTimeField(default=timezone.now)

    def __str__(self):  
        return self.accountname

class AccountPayment(models.Model):    
    # gender choices
    church = models.ForeignKey(ChurchProfile, related_name='accpayment_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branches, related_name='accpayment_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
    memberid = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True )
    payerfullname = models.CharField(max_length=255)
    accountname = models.CharField(max_length=255, default='')	
    accounttype = models.CharField(max_length=100, blank=True, null=True, default='')
    currency = models.CharField(max_length=255, blank=True, null=True)	
    amount = models.CharField(max_length=255, default='')	
    payinby = models.CharField(('Payin By'), max_length=255, blank=False, null=True, default = '')
    paymentmethod = models.CharField(max_length=255, default='')
    cheq_chequenumber = models.CharField(max_length=255, default='', null=True, blank=True)
    cheq_micrcode = models.CharField(max_length=255, default='', null=True, blank=True)
    cheq_accountnumber = models.CharField(max_length=255, default='', null=True, blank=True)
    wirtrans_accountnumber = models.CharField(max_length=255, default='', null=True, blank=True)
    instantpledge = models.BooleanField(blank=True,  default=False)
    deleted = models.BooleanField(blank=False,  default=False)
    datecreated = models.DateTimeField(default=timezone.now)

    def __str__(self):  
        return self.accountname

class AccountExpenditure(models.Model):
    church = models.ForeignKey(ChurchProfile, related_name='accexpenditure_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branches, related_name='accexpenditure_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField(blank=True, null=True )
    title = models.CharField(max_length=255)
    description = models.TextField(default='', blank=False, null=True,)	
    quantity = models.CharField(max_length=255, default='', blank=False, null=True,)	
    amount = models.CharField(max_length=255, default = None)
    approvedby = models.CharField(max_length=255, blank=False, null=True, default='')
    deleted = models.BooleanField(blank=False,  default=False)
    datecreated = models.DateTimeField(default=timezone.now)    

    def __str__(self):  
        return self.title