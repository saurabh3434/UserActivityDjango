# Generated by Django 3.0.8 on 2020-07-08 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20200708_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='time_zone',
            new_name='tz',
        ),
    ]
