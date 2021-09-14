from dashboard.views import (Vehicles_Condition, Vehicles_Consumption,
 Vehicles_Status, Vehicles_Status_Active, 
 Vehicles_Status_Inactive, Vehicles_Status_InShop,
 Vehicles_Condition_Critical, Vehicles_Condition_Good, Vehicles_Condition_Satisfactory)
from django.urls import path

urlpatterns = [
    path("", Vehicles_Status.as_view(), name='all'),
    path("status/Active", Vehicles_Status_Active.as_view(), name='Active'),
    path("status/Inactive", Vehicles_Status_Inactive.as_view(), name='Inactive'),
    path("status/InShop", Vehicles_Status_InShop.as_view(), name='InShop'),
    path("conditions/", Vehicles_Condition.as_view(), name='all_cond'),
    path("conditions/Satisfactory", Vehicles_Condition_Satisfactory.as_view(), name='Satisfactory'),
    path("conditions/Good/", Vehicles_Condition_Good.as_view(), name='Good'),
    path("conditions/Critical/", Vehicles_Condition_Critical.as_view(), name='Critical'),
    path("consumption/", Vehicles_Consumption.as_view(), name='consump')
]