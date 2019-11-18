from rest_framework import response,status,views
from django.shortcuts import render

from foundations.models import Sensor

def s_retrieve_page(request, id):
    return render(request, "sensor/retrieve.html", {
        "instrument_id": int(id),
    })
class RetrieveAPIView(views.APIView):
    def get(self, request, id):
        try:
            instrument = Sensor.objects.get(id=int(id))
            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'id': sensor.id,
                    'name': sensor.name,
                    'time': sensor.time
                       }
                )

        except Exception as e:
            return return response.Response(
                status = status.HTTP_400_BAD_REQUEST,
                data = {
                    'error': str(e),
                       }
                )
