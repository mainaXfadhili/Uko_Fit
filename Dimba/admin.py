from django.contrib import admin
from .models import Group, Turf, Booking

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_created_by', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    filter_horizontal = ('members',)

    def get_created_by(self, obj):
        return obj.created_by.username if obj.created_by else '-'
    get_created_by.short_description = 'Created By'

@admin.register(Turf)
class TurfAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_location', 'price_per_hour')
    search_fields = ('name', 'location')

    def get_location(self, obj):
        return obj.location if obj.location else '-'
    get_location.short_description = 'Location'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'turf', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'turf__name')
