from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   #path('', views.dashboard, name='dashboard'),
   #path('', include('django.contrib.auth.urls')),

]