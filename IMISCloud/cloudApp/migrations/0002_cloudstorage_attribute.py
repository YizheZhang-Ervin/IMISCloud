# Generated by Django 3.0.3 on 2020-05-01 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloudstorage',
            name='attribute',
            field=models.TextField(default='private'),
        ),
    ]
