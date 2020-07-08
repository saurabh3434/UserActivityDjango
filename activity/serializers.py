# This file is for model serializers
from rest_framework import serializers

from activity.models import ActivityPeriod, User


class ActivitySerializer(serializers.ModelSerializer):
    """
    This Serializer class serialize the queryset of ActivityPeriod model
    """
    start_time = serializers.DateTimeField(format="%b %#d %Y  %#I:%M %p")
    end_time = serializers.DateTimeField(format="%b %#d %Y  %#I:%M %p")

    class Meta:
        model = ActivityPeriod
        fields = ("start_time", "end_time",)


class UserSerializer(serializers.ModelSerializer):
    """
    This serializer class is to serialize the queryset of User model
    """
    activity_periods = ActivitySerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
