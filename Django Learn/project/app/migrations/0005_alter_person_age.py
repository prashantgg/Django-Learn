# Generated by Django 5.0.6 on 2024-05-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_person_options_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=''),
        ),
    ]