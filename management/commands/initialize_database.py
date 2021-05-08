from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.create(name='ahmed', employee_number='1254', password='123456')
