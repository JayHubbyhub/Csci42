# Generated by Django 4.1.7 on 2023-03-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_item_assignment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='assignment_image',
        ),
        migrations.AddField(
            model_name='item',
            name='lost_item_image',
            field=models.ImageField(blank=True, null=True, upload_to='lost_items/images'),
        ),
    ]
