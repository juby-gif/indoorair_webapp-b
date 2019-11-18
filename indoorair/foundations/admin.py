from django.contrib import admin
from.models import Instrument,Sensor,TimeSeriesDatum,Report,AirQualityDB
admin.site.register(Instrument)
admin.site.register(Sensor)
admin.site.register(TimeSeriesDatum)
admin.site.register(Report)
admin.site.register(AirQualityDB)
