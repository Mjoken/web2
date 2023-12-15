from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from students.managers import *


# Create your models here.

class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"),
                              unique=True,
                              error_messages={'unique': _("A user is already registered with this email address")})
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    second_name = models.CharField(max_length=55)
    group = models.CharField(max_length=10)
    subgroup = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    id_card = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999999)], blank=False,
                                       null=False, unique=True)
    is_mag = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    objects = StudentUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'second_name', 'group', 'id_card']

    def __str__(self):
        return self.email

    def get_email(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_group(self):
        return self.group

    def get_group_filtered(self):
        group_filtered = str(self.group).lower().replace('-', '')
        return group_filtered

    def get_id_card(self):
        return self.id_card

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'auth_user'
