from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions, routers
from rest_framework.documentation import include_docs_urls
from django.views.generic import RedirectView

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from administration.views import ChoicesViewSet, ChurchGroupsViewSet
from attendance.views import AttendanceProgramsViewSet, AttendancesViewSet
from finance.views import AccountExpenditureViewSet, AccountPaymentViewSet, AccountSetupViewSet
from guests.views import GuestsViewSet
from index.views import EmailSubscriptionsViewSet, FeaturesViewSet, TestimoniesViewSet
from members.views import MembersViewSet
from branches.views import BranchUserViewSet, BranchesViewSet
from churchprofile.views import ProfileViewSet, RegisterViewSet
from notifier.views import EmailSentsViewSet, NotifierSettingssViewSet, PushSentsViewSet, SmsSentsViewSet, TelephonyViewSet
from reports.views import BranchReportsViewSet
from techpanel.views import AdvancedUsersViewSet, SalesUserAccountsViewSet, SalesViewSet, TechChatTicketsViewSet, TechChatsViewSet

# v1 Routers
router_v1 = routers.DefaultRouter(trailing_slash=False)

# Administration
router_v1.register(r'administration', ChurchGroupsViewSet, basename='churchgroups')
router_v1.register(r'administration', ChoicesViewSet, basename='choices')

# Attendance
router_v1.register(r'attendance', AttendanceProgramsViewSet, basename='attendanceprograms')
router_v1.register(r'attendance', AttendancesViewSet, basename='attendances')

# Member
router_v1.register(r'members', MembersViewSet, basename='members')

# Branches
router_v1.register(r'branches', BranchesViewSet, basename='branches')
router_v1.register(r'branches', BranchUserViewSet, basename='branchuser')

# Church
router_v1.register(r'register', RegisterViewSet, basename='register')
router_v1.register(r'churchprofile', ProfileViewSet, basename='churchprofile')

# Finance
router_v1.register(r'accountsetup', AccountSetupViewSet, basename='accountsetup')
router_v1.register(r'accountpayment', AccountPaymentViewSet, basename='accountpayment')
router_v1.register(r'accountexpenditure', AccountExpenditureViewSet, basename='accountexpenditure')

# Guests
router_v1.register(r'guests', GuestsViewSet, basename='guests')

# Index
router_v1.register(r'testimonies', TestimoniesViewSet, basename='testimonies')
router_v1.register(r'features', FeaturesViewSet, basename='features')
router_v1.register(r'emailsubscriptions', EmailSubscriptionsViewSet, basename='emailsubscriptions')

# Notifier
router_v1.register(r'notifiersettings', NotifierSettingssViewSet, basename='notifiersettings')
router_v1.register(r'smssent', SmsSentsViewSet, basename='smssent')
router_v1.register(r'emailsent', EmailSentsViewSet, basename='emailsent')
router_v1.register(r'pushsent', PushSentsViewSet, basename='pushsent')
router_v1.register(r'telephony', TelephonyViewSet, basename='telephony')

# Reports
router_v1.register(r'branchreports', BranchReportsViewSet, basename='branchreports')

# Techpanel
router_v1.register(r'advancedusers', AdvancedUsersViewSet, basename='advancedusers')
router_v1.register(r'salesuseraccounts', SalesUserAccountsViewSet, basename='salesuseraccounts')
router_v1.register(r'sales', SalesViewSet, basename='sales')
router_v1.register(r'techchattickets', TechChatTicketsViewSet, basename='techchattickets')
router_v1.register(r'techchats', TechChatsViewSet, basename='techchats')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('v1/', include([
        path('', include(router_v1.urls)),
    ])),
    path('', RedirectView.as_view(pattern_name='docs')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularRedocView.as_view(url_name='schema'), name='docs'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)