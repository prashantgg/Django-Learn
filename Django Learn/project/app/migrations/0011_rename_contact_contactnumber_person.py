# Generated by Django 5.0.6 on 2024-05-22 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_contactnumber_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactnumber',
            old_name='contact',
            new_name='person',
        ),
    ]
