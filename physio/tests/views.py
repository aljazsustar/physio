from rest_framework import generics

from tests.models import Test
from tests.serializers import TestSerializer


class TestViewSet(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
