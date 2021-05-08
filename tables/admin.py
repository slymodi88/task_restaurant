from django.contrib import admin

from tables.models import Table, Reservation, WorkingHour


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_num','num_seats')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(WorkingHour)
class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ('start_day','end_day')


