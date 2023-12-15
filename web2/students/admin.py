# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

from students.forms import CustomUserCreationForm, CustomUserChangeForm

class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Student
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    list_display = ['email', 'id_card', 'group', 'first_name', 'last_name', 'second_name']
    ordering = ('email',)

admin.site.register(Student, MyUserAdmin)
