from rest_framework import generics

from patients.models import Patient
from patients.serializers import PatientSerializer


class PatientsViewSet(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
