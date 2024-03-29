# Generated by Django 4.2 on 2023-04-18 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('category', models.CharField(default='Umbrella', max_length=100)),
                ('form', models.FileField(upload_to='files/')),
                ('isChecked', models.BooleanField(default=False)),
                ('submissionDate', models.DateTimeField(default=datetime.datetime(2023, 4, 18, 14, 8, 51, 76978))),
            ],
        ),
    ]
