# Generated by Django 4.2.11 on 2024-10-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='events', to='events.participant'),
        ),
    ]
