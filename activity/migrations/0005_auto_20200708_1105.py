# Generated by Django 3.0.8 on 2020-07-08 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20200708_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='activity',
            new_name='activity_periods',
        ),
    ]
