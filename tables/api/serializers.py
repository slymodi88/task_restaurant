from rest_framework import serializers
from tables.models import Reservation, WorkingHour


class AvailableTimes(serializers.Serializer):
    start_time = serializers.TimeField(format="%H:%M")
    end_time = serializers.TimeField(format="%H:%M")


class ReservationSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format="%H:%M", required=True)
    end_time = serializers.TimeField(format="%H:%M", required=True)


    class Meta:
        model = Reservation
        fields = ('id', 'start_time', 'end_time', 'table',)

    def validate(self, data):
        """

        check that the entered data is in the restaurant working hours
        """
        start_time = data.get("start_time")
        end_time = data.get("end_time")
        working_hours = WorkingHour.objects.first()
        if start_time < working_hours.start_day:
            raise serializers.ValidationError(
                'start time must be in working hours'
            )
        if end_time > working_hours.end_day:
            raise serializers.ValidationError(
                'end time must be in working hours'
            )

        return data
