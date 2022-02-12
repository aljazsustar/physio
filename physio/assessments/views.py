from rest_framework import generics

from assessments.models import Assessment
from assessments.serializers import AssessmentSerializer


class AssessmentsRetireveCreateView(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class AssessmentDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

