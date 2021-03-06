# Generated by Django 3.2.8 on 2021-11-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='DOB',
            field=models.TextField(default='', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.TextField(default='Male', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.TextField(default='', max_length=255),
        ),
    ]
