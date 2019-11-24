from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response, views, status

from foundations.models import Instrument
from .serializers import DashboardSerializer


def dashboard_page(request):
    return render(request, "dashboard/dashboard.html", {
        'user': request.user,
    })


class DashboardAPI(views.APIView):
    def get(self, request):
        instruments = Instrument.objects.filter(user=request.user)
        serializer = DashboardSerializer(instruments)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
