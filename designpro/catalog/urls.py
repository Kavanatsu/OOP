from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationAllListView, name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('accounts/profile/', views.ApplicationListView, name='profile'),
]
