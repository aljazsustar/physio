from rest_framework import serializers

from patients.models import Patient
from tests.serializers import TestSerializer


class PatientSerializer(serializers.ModelSerializer):

    tests = TestSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ('id', 'name', 'last_name', 'age', 'diagnosys', 'functional_state', 'tests')
