# Generated by Django 5.0.6 on 2024-05-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone_no',
            field=models.CharField(default='', max_length=20),
        ),
    ]