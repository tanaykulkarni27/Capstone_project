# Generated by Django 3.2.8 on 2021-11-01 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211031_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.TextField(default='', max_length=255),
        ),
    ]