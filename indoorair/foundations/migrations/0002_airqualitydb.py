# Generated by Django 2.2.7 on 2019-11-16 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirQualityDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=20)),
                ('value', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
