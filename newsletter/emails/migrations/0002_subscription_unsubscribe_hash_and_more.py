# Generated by Django 4.2.3 on 2023-07-03 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='unsubscribe_hash',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 16, 16, 23, 601797)),
        ),
    ]