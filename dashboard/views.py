from dashboard.serializers import VehicleSerializer, ConsSerializer
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Vehicle, Consum
from django.db.models import Sum


# Create your views here.


class Vehicles_Status(ListCreateAPIView):
    # queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     status = ['Active', 'Inactive', 'InShop']
    #     status_nums = []
    #     for s in status:
    #         status_nums.append({s: len(Vehicle.objects.all().filter(status=s))})
    #     queryset = status_nums
    #     # queryset = Vehicle.objects.all()
    #     # status = self.kwargs.get('status', None)
    #     # if username is not None:
    #     #     queryset = queryset.filter(provider_id=username)
    #     return queryset


class Vehicles_Status_Active(ListCreateAPIView):
    queryset = Vehicle.objects.all().filter(status="Active")
    serializer_class = VehicleSerializer


class Vehicles_Status_Inactive(ListCreateAPIView):
    queryset = Vehicle.objects.all().filter(status="Inactive")
    serializer_class = VehicleSerializer


class Vehicles_Status_InShop(ListCreateAPIView):
    queryset = Vehicle.objects.all().filter(status="InShop")
    serializer_class = VehicleSerializer


class Vehicles_Condition(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class Vehicles_Condition_Satisfactory(ListCreateAPIView):
    queryset = Vehicle.objects.all().filter(condition="Satisfactory")
    serializer_class = VehicleSerializer

class Vehicles_Condition_Critical(ListCreateAPIView):
    queryset = Vehicle.objects.all().filter(condition="Critical")
    serializer_class = VehicleSerializer

class Vehicles_Condition_Good(ListCreateAPIView):
    queryset = Vehicle.objects.all().filter(condition="Good")
    serializer_class = VehicleSerializer

class Vehicles_Consumption(ListCreateAPIView):
    queryset = Consum.objects.all()
    # .filter(date__day='13')
    serializer_class = ConsSerializer
