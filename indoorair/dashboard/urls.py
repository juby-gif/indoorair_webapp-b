"""
dashboard/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_page, name='dashboard_page'),
    path('api/dashboard', views.DashboardAPI.as_view(), name='dashboard_apis'),
]
