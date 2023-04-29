# Generated by Django 4.0.3 on 2023-04-29 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0004_verification_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='verification',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='verification',
            name='submissionDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 29, 10, 9, 14, 910395)),
        ),
    ]