from django.urls import path
from django.urls import re_path
from . import views
from django.contrib.auth.views import LoginView
app_name='Accounts'
urlpatterns = [
	path('login/', LoginView.as_view()),
	path('register/', views.register),
	path('logout/', views.logout)
]
