# Generated by Django 4.2.16 on 2024-09-26 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/&m/&d/'),
        ),
    ]
