# Generated by Django 3.2.8 on 2021-11-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.TextField(default='', max_length=255),
        ),
    ]