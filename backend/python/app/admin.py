from django.contrib import admin

from .models import Car, Hotel, Booking


# Register your models here.


class AbstractModelAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Car)
class CarAdmin(AbstractModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(AbstractModelAdmin):
    pass


"""
@admin.register(Booking)
class BookingAdmin(AbstractModelAdmin):
    list_display = ('start_date', 'end_date', 'unit')
"""
