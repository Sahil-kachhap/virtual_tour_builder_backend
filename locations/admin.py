from django.contrib import admin
from .models import Location, LocationMedia

class LocationMediaInline(admin.TabularInline):
    model = LocationMedia
    extra = 1

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'tour', 'latitude', 'longitude', 'order')
    list_filter = ('tour',)
    search_fields = ('name', 'description', 'address')
    inlines = [LocationMediaInline]