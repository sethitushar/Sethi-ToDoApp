# Generated by Django 3.0.5 on 2020-06-09 11:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_no', models.CharField(max_length=50)),
                ('lastsavedon', models.DateTimeField()),
                ('lastsavedby', models.EmailField(default=None, max_length=254)),
                ('items', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=1000), size=2), size=None)),
            ],
        ),
    ]