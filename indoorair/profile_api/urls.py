from django.urls import path

from . import views


urlpatterns = [

path('retrieve_profile',views.profile_retrieve_page, name = 'retrieve_profile_page'),
path('api/retrieve_profile',views.ProfileAPIView.as_view),
path('api/update_profile',views.ProfileUpdateAPIView.as_view()),
]
