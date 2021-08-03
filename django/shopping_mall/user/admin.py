from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'register_date')


admin.site.register(User, UserAdmin)
