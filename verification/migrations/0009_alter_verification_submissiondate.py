# Generated by Django 4.1.7 on 2023-03-27 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0008_alter_verification_submissiondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='submissionDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 27, 17, 56, 51, 894680)),
        ),
    ]