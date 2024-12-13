from django.contrib import admin
from .models import Turf, Group, Contact

@admin.register(Turf)
class TurfAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'price_per_hour')
    search_fields = ('name', 'address')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
