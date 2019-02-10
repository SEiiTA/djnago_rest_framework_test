from django.contrib import admin

from blog.models import User, Entry


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass
