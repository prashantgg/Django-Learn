# Generated by Django 5.0.6 on 2024-05-22 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_contactnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactnumber',
            name='contact',
        ),
    ]