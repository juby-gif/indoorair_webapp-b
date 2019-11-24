"""
gateway/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login, logout
from rest_framework import views, status, response

from gateway.serializers import RegisterSerializer, LoginSerializer


def register_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "gateway/register.html", {})


def register_success_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "gateway/register_success.html", {})


def login_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "gateway/login.html", {})


class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data,
        )



class LoginAPI(views.APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={
            'request': request,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                 'details': 'You have been logged in successfully!'
            },
        )



def logout_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "gateway/logout.html", {})


def post_logout_api(request):
    try:
        logout(request)
        return JsonResponse({
             "was_logged_out": True,
             "reason": None,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
             "was_logged_out": False,
             "reason": str(e),
        })
