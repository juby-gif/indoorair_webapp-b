"""
report/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('reports', views.report_list_page, name='report_list_page'),
    path('report/1', views.report_01_page, name='report_01_page'),
    path('report/api/1', views.download_csv_report_01_temperature_sensor_api, name="download_csv_report_01_temperature_sensor_api")
    # path('api/version', views.get_version_api, name='version_api'),
]
