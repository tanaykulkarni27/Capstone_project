# Generated by Django 3.2.8 on 2021-11-04 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20211103_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
    ]