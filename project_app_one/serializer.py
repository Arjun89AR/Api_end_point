from rest_framework import serializers
from . models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    REMIND_BY_CHOICES=('sms', 'email')

    remind_by = serializers.ChoiceField(choices=REMIND_BY_CHOICES)

    class Meta:
        model = Reminder
        fields ='__all__'