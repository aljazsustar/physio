# Generated by Django 4.0.1 on 2022-01-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_remove_test_fields_testattribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testattribute',
            name='attribute_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testattribute',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testattribute',
            name='unit',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]
