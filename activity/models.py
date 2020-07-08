from django.db import models
import pytz

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


# Create your models here.


class ActivityPeriod(models.Model):
    """
    Model to store Actvity start and end time of user
    """
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class User(models.Model):
    """
    models to store user details
    """
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=20, null=False)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    activity_periods = models.ManyToManyField(ActivityPeriod, null=True)

