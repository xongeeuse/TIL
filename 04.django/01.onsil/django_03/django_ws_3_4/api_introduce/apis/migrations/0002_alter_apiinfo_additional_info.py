# Generated by Django 4.2.11 on 2024-09-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinfo',
            name='additional_info',
            field=models.JSONField(),
        ),
    ]
