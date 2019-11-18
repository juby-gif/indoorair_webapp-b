from django.urls import path

from . import views


urlpatterns = [

path('sensor/retrieve',views.s_retrieve_page, name = 'retrieve_sensor_page'),
path('api/retrieve',views.RetrieveAPIView.as_view()),
]
