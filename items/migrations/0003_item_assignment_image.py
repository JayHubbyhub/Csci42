# Generated by Django 4.1.7 on 2023-03-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='assignment_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
