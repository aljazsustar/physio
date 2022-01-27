from django.urls import path
from .views import TestViewSet, TestAttributeListCreateViewSet

app_name = "tests"

urlpatterns = [
    path("", TestViewSet.as_view(), name='test_list'),
    path("attributes", TestAttributeListCreateViewSet.as_view(), name='test_attributes'),
]
