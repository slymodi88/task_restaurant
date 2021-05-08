import jwt
from django.contrib.auth.base_user import BaseUserManager

from resturant_task import settings


class UserManager(BaseUserManager):
    def create_user(self, employee_number, password=None):
        if not employee_number:
            raise ValueError('employee number required')

        user = self.model(
            employee_number=employee_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_number, password):
        user = self.create_user(
            employee_number,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_token(self, user):
        payload = {'id': user.id, 'employee_number': user.employee_number}
        token = jwt.encode(
            payload, settings.SECRET_KEY)
        user.token = bytes.decode(token)
        user.save()
        return user
