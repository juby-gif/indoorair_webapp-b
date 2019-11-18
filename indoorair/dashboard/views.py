from rest_framework import views,response,status
from django.shortcuts import render
from django.http import JsonResponse

from dashboard.serializers import AverageCalculatorSerializer,AddSerializer
from foundations.models import AirQualityDB


def dashboard_page(request):
    return render(request, "dashboard/dashboard.html", {})
class DashboardAPIView(views.APIView):

    def post(self, request):
        # if request.user.is_authenticated:
        serializer = AddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
        status = status.HTTP_200_OK,
        data = {
        'message': 'We have successfully added the sensor'
        }
        )

    def get(self, request):
        # if request.user.is_authenticated:

        try:
            temp_data = AirQualityDB.objects.filter(name='TEMPERATURE').values_list('value', flat=True)
            humid_data = AirQualityDB.objects.filter(name='HUMIDITY').values_list('value', flat=True)
            press_data = AirQualityDB.objects.filter(name='PRESSURE').values_list('value', flat=True)
            co2_data = AirQualityDB.objects.filter(name='CO2').values_list('value', flat=True)
            tvoc_data = AirQualityDB.objects.filter(name='TVOC').values_list('value', flat=True)
        except Exception as e:
            return response.Response(
            status = status.HTTP_400_BAD_REQUEST,
            data = {
                'message': str(e)
                }
            )
        avg_temp = AverageCalculatorSerializer(temp_data, many=False)
        avg_humid = AverageCalculatorSerializer(humid_data, many=False)
        avg_press = AverageCalculatorSerializer(press_data, many=False)
        avg_co2 = AverageCalculatorSerializer(co2_data, many=False)
        avg_tvoc = AverageCalculatorSerializer(tvoc_data, many=False)


        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'Temperature Sensor': 'Average Temperature = ' + avg_temp.data,
                'Humidity Sensor': 'Average Humidity = ' + avg_humid.data,
                'Pressure Sensor': 'Average Pressure = ' + avg_press.data,
                'CO2 Sensor': 'Average CO2 = ' + avg_co2.data,
                'TVOC Sensor': 'Average TVOC = ' + avg_tvoc.data,
            }
        )
