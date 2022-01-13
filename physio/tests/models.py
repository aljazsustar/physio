from django.db import models

from patients.models import Patient


class Test(models.Model):
    test_name = models.CharField(max_length=255)
    fields = models.JSONField()
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

