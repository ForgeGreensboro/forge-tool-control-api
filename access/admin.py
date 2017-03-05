from django.contrib import admin

from access.models import AccessLevel, Machine, Profile
from access.models import LogEntry, Department, Reservation


admin.site.register(AccessLevel)
admin.site.register(Machine)
admin.site.register(Profile)
admin.site.register(LogEntry)
admin.site.register(Department)
admin.site.register(Reservation)
