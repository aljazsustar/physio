# Generated by Django 4.0.1 on 2022-01-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='diagnosys',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='functional_state',
            field=models.TextField(default=''),
        ),
    ]