from django.contrib import admin

from appointments.models import Appointment, Billing, Doctor, Facility, Patient, Prescription

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Billing)
admin.site.register(Facility)
