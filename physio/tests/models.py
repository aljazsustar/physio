from django.db import models

from patients.models import Patient


class Test(models.Model):
    test_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.test_name} ({self.id})'


class TestAttribute(models.Model):
    attribute_name = models.CharField(max_length=255)
    attribute_value = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=63, default=0.0)
    remarks = models.TextField(blank=True, null=True)
    test = models.ForeignKey(Test, on_delete=models.PROTECT, related_name='attributes')


