from django.contrib import admin
from .models import Event, Session, Track, Attendee

admin.site.register(Event)
admin.site.register(Session)
admin.site.register(Track)
admin.site.register(Attendee)