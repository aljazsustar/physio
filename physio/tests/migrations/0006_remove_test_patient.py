# Generated by Django 4.0.1 on 2022-01-30 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_alter_test_patient_alter_testattribute_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='patient',
        ),
    ]
