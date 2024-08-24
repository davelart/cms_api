from django.contrib import admin
from .models import EmailSent, NotifierSettings, PushSent, SmsSent, Telephony

@admin.register(SmsSent)
class SmsSentAdmin(admin.ModelAdmin):
	search_fields = ('senderid', 'accordingto', 'datecreated', 'message')
	list_display = ('senderid', 'accordingto', 'datecreated', 'branch', 'church')

@admin.register(EmailSent)
class EmailSentAdmin(admin.ModelAdmin):
	search_fields = ('fromaddr', 'subject', 'accordingto', 'datecreated', 'message')
	list_display = ('fromaddr', 'subject', 'accordingto', 'datecreated', 'branch', 'church')

@admin.register(PushSent)
class PushSentAdmin(admin.ModelAdmin):
	search_fields = ('church', 'branch', 'title', 'message', 'deviceid', 'accordingto', 'mediafile', 'datecreated')
	list_display = ('church', 'branch', 'title', 'message', 'deviceid', 'accordingto', 'mediafile', 'datecreated')

@admin.register(NotifierSettings)
class NotifierSettingsAdmin(admin.ModelAdmin):
	search_fields = ('sms_sender', 'email_from', 'church__churchname', 'branch__branchname')
	list_display = ('church', 'branch', 'sms_sender', 'email_from', 'notifierpoints')

@admin.register(Telephony)
class TelephonyAdmin(admin.ModelAdmin):
	search_fields = ('countrycode', 'country', 'supportednetworks', 'nonetstartwith')
	list_display = ('countrycode', 'country', 'supportednetworks', 'nonetstartwith')

