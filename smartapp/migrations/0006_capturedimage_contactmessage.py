# Generated by Django 5.0.4 on 2024-05-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0005_alter_customuser_car_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapturedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=255)),
                ('captured_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
