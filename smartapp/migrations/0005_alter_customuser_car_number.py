# Generated by Django 5.0.4 on 2024-05-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0004_parkingcenter_contact_parkingcenter_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='car_number',
            field=models.CharField(max_length=20),
        ),
    ]
