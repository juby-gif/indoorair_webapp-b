from django.urls import path

from . import views


urlpatterns = [
    path('login', views.login_page, name='login_page'),
    path('register',views.register_page, name = 'register_page'),
    path('register/ok',views.register_success, name = 'registered_page'),
    path('api/login',views.LoginAPIView.as_view()),
    path('api/register',views.RegisterAPIView.as_view()),
    path('logout', views.logout_page, name='logout_page'),
    path('api/logout', views.LogoutAPIView.as_view()),
]
