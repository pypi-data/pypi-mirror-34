# Generated by Django 2.0.7 on 2018-07-06 09:40

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rayures', '0001_squashed_0005_auto_20180630_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderReturn',
            fields=[
                ('id', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False)),
                ('api_version', models.CharField(editable=False, max_length=12)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
