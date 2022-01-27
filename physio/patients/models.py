from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    diagnosys = models.TextField(default="")
    functional_state = models.TextField(default="")

    def __str__(self):
        return f'{self.name} {self.last_name} ({self.id})'
