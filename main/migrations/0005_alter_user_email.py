# Generated by Django 3.2.8 on 2021-11-01 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211031_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='tanay@gmail.com', max_length=255, unique=True),
        ),
    ]
