from django.db import models

from patients.models import Patient
from tests.models import Test


class Assessment(models.Model):
    patient = models.ForeignKey(Patient, models.PROTECT, related_name='assessment')
    tests = models.ManyToManyField(Test)
