from rest_framework import views,response,status
from django.shortcuts import render


def profile_retrieve_page(request):
    return render(request, "userprofile/retrieve.html", {})

class ProfileAPIView(views.APIView):
    def get(self, request):
        try:
            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'username': request.user.username,
                      }
                )
        except Exception as e:
            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'error': str(e),
                      }
                )

def profile_update_page(request):
    return render(request, "userprofile/update.html", {})

class ProfileUpdateAPIView(views.APIView):
    def post(self, request):
        try:
            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'message':'Profile updated successfully!'
                       }
                )
        except Exception as e:
            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'error':str(e)
                       }
                )
