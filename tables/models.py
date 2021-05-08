from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date


class Table(models.Model):
    """
    Table model is used to hold information about tables in the restaurant such as table number and numer of seats on each
    table
    table_num integer field with mam value of 4 is used to hold the number of the table in the restaurant
    num_seats integer field with mam value of 6 is used to hold the number of the seats  on a table
    """
    table_num = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(4)])
    num_seats = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(6)])

    def __str__(self):
        return str(self.table_num)


class Reservation(models.Model):
    """
    reservation model to store each  reservation data as its start and end time,date, table number

    start_time field holds the reservation starting time
    end_time field holds the reservation ending time
    reservation_date field to store which day the reservation will take place
    table is a foreignkey field to implement the ont to many relationship between each Table and its reservations
    """
    start_time = models.TimeField()
    end_time = models.TimeField()
    reservation_date = models.DateField(auto_created=True, default=str(date.today()))
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.pk)


class WorkingHour(models.Model):
    """
    WorkingHour model to store the start and end working hours of a day
    """
    start_day = models.TimeField()
    end_day = models.TimeField()

    def __str__(self):
        return str(self.pk)
