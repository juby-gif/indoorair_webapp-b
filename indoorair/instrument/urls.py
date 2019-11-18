from django.urls import path

from . import views

urlpatterns = [
    path('instrument/create', views.i_create_page, name='i_create_page'),
    path('instruments', views.i_list_page, name='i_list_page'),
    path('instrument/<id>', views.i_retrieve_page, name='i_retrieve_page'),
    path('instrument/<id>/update', views.i_update_page, name='i_update_page'),
    path('api/create', views.CreateAPIView.as_view()),
    path('api/instruments', views.ListInstrumentsAPIView.as_view()),
    path('api/instrument/<id>', views.RetrieveAPIView.as_view()),
    path('api/instrument/<id>/update', views.UpdateAPIView.as_view()),
]
