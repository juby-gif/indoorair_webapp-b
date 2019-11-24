"""
sensor/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('sensor/<int:id>', views.sensor_retrieve_page, name='sensor_retrieve_page'),
    path('api/sensor/<int:id>', views.SensorRetrieveAPI.as_view(), name='sensor_retrieve_api')
]
