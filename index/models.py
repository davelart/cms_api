from django.db import models
from django.utils import timezone

from index.utils import *

class Testimonies(models.Model):
	fullname = models.CharField(max_length=255, blank=True, null=True )
	subinfo = models.CharField(max_length=255, blank=True, null=True )
	testimony = models.TextField(blank=True, null=True )
	photograph = models.ImageField(upload_to='testimoniesmedia', max_length=255, blank=True, null=True)
	activestatus = models.BooleanField(blank=True,  default=True)
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		return self.fullname

        
class Features(models.Model):
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    featureshortname = models.CharField(max_length=100, blank=True, null=True)
    featurelongname = models.CharField(max_length=255, blank=True, null=True)
    featureicon = models.ImageField(upload_to='featuresmedia', max_length=255, blank=True, null=True)
    featureshortdescription = models.TextField(blank=True, null=True)
    featurelongdescription = models.TextField(blank=True, null=True)
    ordernumber = models.CharField(max_length=100, blank=True, null=True)
    featurecolor = models.CharField(max_length=100, blank=True, null=True)
    activestatus = models.BooleanField(blank=True, default=True)
    datecreated = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        try:
            if not self.is_update_view:
                self.slug = generate_slug(self, self.featureshortname)
        except:
            self.slug = generate_slug(self, self.featureshortname)
        
        super(Features, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.slug


class EmailSubscription(models.Model):
    email = models.EmailField(max_length=255, blank=False, null=True)
    subscriptionstatus = models.BooleanField(max_length=255, blank=True, default=False )
    code = models.CharField(max_length=255, blank=False, null=True)
    datecreated = models.DateTimeField(default=timezone.now)


    def __str__(self):  
        return self.email