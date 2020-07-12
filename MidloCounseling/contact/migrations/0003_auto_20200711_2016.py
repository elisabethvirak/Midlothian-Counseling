# Generated by Django 3.0.3 on 2020-07-12 00:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200710_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='author',
        ),
        migrations.RemoveField(
            model_name='interest',
            name='title',
        ),
        migrations.AddField(
            model_name='interest',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='interest',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 0, 16, 28, 434031, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='interest',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 0, 16, 28, 434031, tzinfo=utc)),
        ),
    ]