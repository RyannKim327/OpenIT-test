from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserConfig(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {"fields": ("first_name", "middle_name", "last_name", "sex")},
        ),
    )
