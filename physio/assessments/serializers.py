from rest_framework import serializers

from assessments.models import Assessment


class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment
        fields = ('id', 'patient', 'tests')
