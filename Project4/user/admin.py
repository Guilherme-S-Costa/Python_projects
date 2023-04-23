from django.contrib import admin
from user.models import User

admin.site.register(User)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     readonly_fields = ('nome', 'email', 'senha')
