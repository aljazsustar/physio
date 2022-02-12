from django.urls import path
from .views import PatientsViewSet, PatientDeleteUpdateView

app_name = "patients"

urlpatterns = [
    path("", PatientsViewSet.as_view(), name='patients_list'),
    path("<int:pk>", PatientDeleteUpdateView.as_view(), name='patient'),
    path("<int:pk>/tests", PatientsViewSet.as_view(), name='patient_tests'),
    path("<int:patient>/tests/<int:pk>", PatientDeleteUpdateView.as_view(), name='patient_test'),
]
