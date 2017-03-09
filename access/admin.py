from django.contrib import admin

from .models import AccessLevel, Profile, Department, Reservation, Machine
from .models import LogEntry


admin.site.register(AccessLevel)
admin.site.register(Machine)
admin.site.register(Profile)
admin.site.register(LogEntry)
admin.site.register(Department)
admin.site.register(Reservation)
