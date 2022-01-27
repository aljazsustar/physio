# Generated by Django 4.0.1 on 2022-01-27 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='fields',
        ),
        migrations.CreateModel(
            name='TestAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=255)),
                ('attribute_value', models.FloatField()),
                ('unit', models.CharField(max_length=63)),
                ('remarks', models.TextField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tests.test')),
            ],
        ),
    ]
