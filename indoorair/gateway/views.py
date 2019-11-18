from django.contrib.auth import authenticate,login,logout
from rest_framework import views,response,status
from django.shortcuts import render


def login_page(request):
  user = request.user
  context = {
      'user': user,
  }
  return render(request, "gateway/login.html", context)
def register_page(request):
  user = request.user
  context = {
      'user': user,
  }
  return render(request, "gateway/register.html", context)

def register_success(request):
  return render(request, "gateway/register_success.html", {})

def logout_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "gateway/logout.html", {})

class LoginAPIView(views.APIView):
    def post(self, request):
        username = request.data.get('username',None)
        password = request.data.get('password',None)
        print("For debugging purposes", username, password)
        try:
            user = authenticate(username=username, password=password)
            if user:
                print("PRE-LOGIN", user.get_full_name())
                login(request, user)
                print("POST-LOGIN", user.get_full_name())
                return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'message': str(user.get_first_name())+'is Logged-in Successfully!'
                }
                )

            else:
                return response.Response(
                status=status.HTTP_400_BAD_REQUEST,
                data = {
                'error':'Login Failed.Please check your username or password and try again!'
                       }
                       )
        except Exception as e:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data = {
            'error':str(e)
                   }
                   )


class RegisterAPIView(views.APIView):
    def post(self, request):
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        # This is for debugging purposes only.
        print(first_name, last_name, username, email, password)
        # STEP 3: Plug in our data from the request into our User model.
        try:
          user = User.objects.create_user(username, email, password)
          user.last_name = last_name
          user.first_name = first_name
          user.save()
          return response.Response(
               status = status.HTTP_201_CREATED,
               data={
                'message': 'You have Successfully Registered, Please Log-in!'
                    }
                    )
        except Exception as e:
          return response.Response(
                status = status.HTTP_400_BAD_REQUEST,
                data = {
                    'error!' : str(e)
                       }
                       )


class LogoutAPIView(views.APIView):
    def post(self, request):
        try:
            logout(request)
            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'message' : 'You have logged out Successfully!'
                       }
                       )
        except Exception as e:
            print(e)
            return response.Response(
                    status = status.HTTP_400_BAD_REQUEST,
                    data = {
                        'error' : str(e)
                           }
                           )
