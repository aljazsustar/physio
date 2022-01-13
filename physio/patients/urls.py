from django.urls import path
from .views import PatientsViewSet

app_name = "patients"

urlpatterns = [
    path("", PatientsViewSet.as_view(), name='patients_list'),
]
