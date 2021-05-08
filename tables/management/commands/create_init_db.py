from django.core.management.base import BaseCommand, CommandError
from tables.models import WorkingHour,Table
from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        WorkingHour.objects.get_or_create(start_day="12:00",end_day="23:59")
        Table.objects.get_or_create(table_num=1,num_seats=2)
        Table.objects.get_or_create(table_num=2,num_seats=2)
        Table.objects.get_or_create(table_num=3,num_seats=4)
        Table.objects.get_or_create(table_num=4,num_seats=6)
        if not User.objects.filter(employee_number="5555", is_superuser=True).exists():
            User.objects.create_superuser("5555", "test1234")




