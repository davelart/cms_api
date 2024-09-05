# church/urls.py
from django.urls import path, include
from .views import SignInViewSet, SignUpViewSet, ResetPasswordViewSet, ResetPasswordConfirmViewSet
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/', include([
        path('signin', SignInViewSet.as_view(), name='user_signin'),
        path('signup', SignUpViewSet.as_view(), name='church_signup'),
        path('refresh-token', TokenRefreshView.as_view(), name='user_refresh_token'),
        path('reset-password', ResetPasswordViewSet.as_view(), name='user_reset_password'),
        path('reset-password-confirm', ResetPasswordConfirmViewSet.as_view(), name='user_reset_password_confirm'),
    ]))
]