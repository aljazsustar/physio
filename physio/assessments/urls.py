from django.urls import path
from .views import AssessmentDeleteUpdateView, AssessmentsRetireveCreateView

app_name = "assessments"

urlpatterns = [
    path("", AssessmentsRetireveCreateView.as_view(), name='assessments_list'),
    path("<int:pk>", AssessmentDeleteUpdateView.as_view(), name='assessment'),
]
