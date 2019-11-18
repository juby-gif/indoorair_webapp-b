from django.urls import path

from . import views


urlpatterns = [

path('retrieve_profile',views.retrieve_profile_page, name = 'retrieve_profile_page'),
path('api/retrieve_profile',views.ProfileAPIView.as_view()),
path('update_profile',views.update_profile_page, name = 'update_profile_page'),
path('api/update_profile',views.ProfileUpdateAPIView.as_view()),
]
