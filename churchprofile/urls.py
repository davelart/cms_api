from django.urls import path, include
from .views import *

from profile import views

urlpatterns = [
    path('accounts', include([
        path('', views.Accounts.as_views(), name='accounts'),
    ]))
]