from django.urls import path
from .views import TestViewSet

app_name = "tests"

urlpatterns = [
    path("", TestViewSet.as_view(), name='test_list'),
]
