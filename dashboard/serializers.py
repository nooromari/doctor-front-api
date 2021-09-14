from django.db.models import fields
from rest_framework import serializers
from .models import Consum, Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'status', 'condition')
        model = Vehicle

class ConsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('consumption', 'date')
        model = Consum