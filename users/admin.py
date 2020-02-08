from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Profile

class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'id', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    # These are required
    filter_horizontal = ()
    list_filter = ()
    fieldsets =()

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
