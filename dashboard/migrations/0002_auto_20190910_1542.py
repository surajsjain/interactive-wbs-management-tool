# Generated by Django 2.2.5 on 2019-09-10 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='attachments/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 10, 15, 42, 27, 951579)),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='timeInitiated',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 10, 15, 42, 27, 951169)),
        ),
    ]
