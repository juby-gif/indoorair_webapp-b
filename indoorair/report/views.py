from rest_framework import views, status, response
from django.shortcuts import render
import random, string

from foundations.models import Sensor,TimeSeriesDatum


def report_list_page(request):
    return render(request, "report/list.html", {})

def report_01_page(request):
    return render(request, "report/report_01.html", {})

class TimeseriesDatumReportListAPIView(views.APIView):
    def get(self, request):
        time_series_datum=TimeseriesDatum.objects.filter(user=request.user)
        output = []
        for datum in time_series_datum.all():
            output.append({
                'id': instrument.id,
                'name': instrument.name,
            })
        return response.Response(
            status = status.HTTP_200_OK,
            data = {
                'message' : 'The Reports are Successfully generated!'
                }
            )

class Report01APIView(views.APIView):
    def post(self, request):
        try:
            report_01 = Report.objects.create(
            contents = random_string_generator(size=1000, chars=string.ascii_lowercase + string.digits))

            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'message' : 'The Report_01 is generated Successfully!'
                }
            )
        except Exception as e:
            return response.Response(
                status = status.HTTP_400_BAD_REQUEST,
                data = {
                    'error' : str(e)
                }
            )
