# Generated by Django 5.0.4 on 2024-05-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingspot',
            name='spot_code',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookedspot',
            name='spot_code',
            field=models.CharField(max_length=50),
        ),
    ]