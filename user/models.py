from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator

from user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model is used to hold information about employees that uses the system such as name, employee_number

    """

    name = models.CharField(max_length=255)
    employee_number = models.CharField(max_length=4, unique=True,
                                       validators=[MinLengthValidator(4, 'employee number must be 4 characters long')])
    token = models.CharField(max_length=255, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'employee_number'
