from rest_framework import serializers
from .models import Event, Session, Track, Attendee
from rest_framework.exceptions import ValidationError

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

    def validate(self, data):
        event = data['event']
        start = data['start_time']
        end = data['end_time']

        # cek bentrok
        sessions = Session.objects.filter(event=event)

        for s in sessions:
            if (start < s.end_time and end > s.start_time):
                raise serializers.ValidationError("Session time conflict!")

        return data

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

    def validate(self, data):
        event = data['event']

        # hitung jumlah attendee sekarang
        total = Attendee.objects.filter(event=event).count()

        if total >= event.capacity:
            raise serializers.ValidationError("Event is full!")

        return data