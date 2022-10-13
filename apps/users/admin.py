from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile

import xadmin

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    pass


# class CourseAdmin(admin.ModelAdmin):
#     pass
#
# xadmin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
