"""
api/serializers.py
"""
from rest_framework import serializers # (1) NEED TO IMPORT CLASS
from rest_framework.validators import UniqueValidator
import statistics

from foundations.models import AirQualityDB # (2) OPTIONAL - IMPORT ANY MODELS WE USE
id = serializers.IntegerField(read_only=True)

value = serializers.IntegerField(
     validators = [
     UniqueValidator(queryset=AirQualityDB.objects.all())
     ]
)


class AddSerializer(serializers.Serializer):
    value = serializers.FloatField()
    name = serializers.CharField()
    def create(self, validated_data):
        value = validated_data.get('value')
        name = validated_data.get('name')
        memory = AirQualityDB.objects.create(name= name,value=value)
        return memory


class AverageCalculatorSerializer(serializers.BaseSerializer):

    def to_representation(self, data):
        sum=0
        length_of_memory_elements = len(data)
        for datum in data:
            sum = sum + datum
        try:
            average = sum/length_of_memory_elements
            mode = statistics.mode(data)

        except Exception as e:
            raise serializers.ValidationError('Sorry We cannot divide a number by 0. Please try again!')

        return average,mode
