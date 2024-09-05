from django.db import models
from django.utils import timezone
from branches.models import Branches
from accounts.models import Church

class ChurchGroup(models.Model):
    church = models.ForeignKey(Church, related_name='churchgroups_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branches, related_name='churchgroups_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
    churchgroup = models.CharField(max_length=255, blank=True, null=True)
    datecreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.churchgroup
    
class Choices(models.Model):
    CHOICETYPE = (('Church Group','Church Group'), ('Ministerial Position','Ministerial Position'))
    church = models.ForeignKey(Church, related_name='choices_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branches, related_name='choices_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)	
    choicetype = models.CharField(max_length=50, null=True, blank=True, choices = CHOICETYPE, default = None) 
    choice = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):  
        return str(self.choice)