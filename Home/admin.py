from django.contrib import admin
from .models import Departments,Doctors,Booking
# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'pat_name', 'pat_phone', 'pat_email', 'doc_name', 'booking_date', 'booked_on')


admin.site.register(Booking,BookingAdmin)