from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, response, views

from foundations.models import Sensor
from sensor.serializers import SensorRetrieveSerializer


def sensor_retrieve_page(request, id):
    return render(request, "sensor/retrieve.html", {
        'id': id,
    })


class SensorRetrieveAPI(views.APIView):
    def get(self, request, id):
        sensor = get_object_or_404(Sensor, id=int(id))
        serializer = SensorRetrieveSerializer(sensor)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
