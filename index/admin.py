from django.contrib import admin

from index.models import Testimonies, Features, EmailSubscription

@admin.register(Testimonies)
class TestimoniesAdmin(admin.ModelAdmin):
	search_fields = ('fullname', 'subinfo', 'testimony', 'photograph')
	list_display = ('fullname', 'subinfo', 'testimony', 'photograph')

@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
	search_fields = ('featurelongname', 'featureicon', 'featureshortdescription', 'datecreated')
	list_display = ('featurelongname', 'featureicon', 'featureshortdescription', 'datecreated')

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
	search_fields = ('email', 'subscriptionstatus', 'code', 'datecreated')
	list_display = ('email', 'subscriptionstatus', 'code', 'datecreated')

