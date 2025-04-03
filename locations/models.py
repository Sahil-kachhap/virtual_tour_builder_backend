from django.db import models
from django.conf import settings
from tours.models import Tour

class Location(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_locations')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    panorama_id = models.CharField(max_length=255, blank=True, null=True)
    heading = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pitch = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} - {self.tour.title}"

class LocationMedia(models.Model):
    MEDIA_TYPES = (
        ('IMAGE', 'Image'),
        ('VIDEO', 'Video'),
        ('AUDIO', 'Audio'),
    )
    
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='location_media/')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.location.name}"