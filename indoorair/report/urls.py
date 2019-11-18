from django.urls import path

from . import views


urlpatterns = [
path('report_list',views.report_list_page, name = 'report_list_page'),
path('report_01',views.report_01_page, name = 'report_01_page'),
path('api/report_list',views.TimeseriesDatumReportListAPIView.as_view()),
path('api/report_01',views.Report01APIView.as_view()),
]
