from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


# Register your models here.
# Admin model to manage users with new User definition
@admin.register(User)
class UserAdmin(BaseUserAdmin):
  add_fieldsets = (
      (
          None,
          {
              "classes": ("wide",),
              "fields": ("username",
                         "password1",
                         "password2",
                         "email",
                         "first_name",
                         "last_name"),
          },
      ),
  )
