from django.contrib import admin

# Register your models here.
from activity.models import User, ActivityPeriod

admin.site.register(ActivityPeriod)
admin.site.register(User)
