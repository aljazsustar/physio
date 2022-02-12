from django.urls import path
from .views import TestViewSet, TestDestroyUpdateView, TestAttributeListCreateViewSet, TestAttributeDestroyUpdateView

app_name = "tests"

urlpatterns = [
    path("", TestViewSet.as_view(), name='test_list'),
    path("<int:pk>", TestDestroyUpdateView.as_view(), name='test'),
    path("<int:test>/attributes", TestAttributeListCreateViewSet.as_view(), name='test_attributes'),
    path("<int:test>/attributes/<int:pk>", TestAttributeDestroyUpdateView.as_view(), name='test_attribute'),
]
