from django.db import models
import uuid
from django.contrib.auth.models import User

class AirQualityDB(models.Model):
    name = models.CharField(max_length = 20)
    value = models.IntegerField()


def get_next():
    return uuid.uuid4()

class Instrument(models.Model):
    user = models.ForeignKey(
          User,
          on_delete=models.CASCADE
          )
    name = models.CharField(max_length=255)
    serial_no = models.UUIDField(primary_key=True, default=get_next, editable=False)

    def __str__(self):
        return self.name + "    " + str(self.user) + "    " + str(self.serial_no)

class Sensor(models.Model):
    instrument = models.ForeignKey(
                 to='Instrument',
                 on_delete=models.CASCADE
                 )
    name = models.CharField(max_length=255)
    def _str_(self):
        return self.name + " " + str(self.instrument)

class TimeSeriesDatum(models.Model):

    sensor = models.ForeignKey( # one-to-many
           to='Sensor',
           on_delete=models.CASCADE
           )
    value = models.FloatField()
    time = models.DateTimeField()
    def __str__(self):
        return str(self.sensor) + "  " + str(self.value) + "  " + str(self.time)

class Report(models.Model):
    report = models.TextField()
    def __str__(self):
        return str(self.report)
