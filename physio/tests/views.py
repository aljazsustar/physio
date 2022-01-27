from rest_framework import generics

from tests.models import Test, TestAttribute
from tests.serializers import TestSerializer, TestAttributeSerializer


class TestViewSet(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestAttributeListCreateViewSet(generics.ListCreateAPIView):
    queryset = TestAttribute.objects.all()
    serializer_class = TestAttributeSerializer
