# Generated by Django 5.0.6 on 2024-05-22 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_contactnumber_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactnumber',
            name='person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.person'),
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('persons', models.ManyToManyField(to='app.person')),
            ],
        ),
    ]
