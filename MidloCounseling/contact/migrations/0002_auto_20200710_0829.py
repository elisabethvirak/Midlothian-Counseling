# Generated by Django 3.0.3 on 2020-07-10 12:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 12, 29, 11, 588091, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='interest',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 12, 29, 11, 587064, tzinfo=utc)),
        ),
    ]
