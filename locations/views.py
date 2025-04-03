# locations/views.py
from rest_framework import viewsets, permissions
from .models import Location, LocationMedia
from .serializers import LocationSerializer, LocationMediaSerializer
from permissions.permission import IsAdminOrEditor

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrEditor]
    
    def get_queryset(self):
        return Location.objects.filter(tour__slug=self.kwargs['tour_slug'])
    
    def perform_create(self, serializer):
        from tours.models import Tour
        tour = Tour.objects.get(slug=self.kwargs['tour_slug'])
        serializer.save(tour=tour)

class LocationMediaViewSet(viewsets.ModelViewSet):
    serializer_class = LocationMediaSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrEditor]
    
    def get_queryset(self):
        return LocationMedia.objects.filter(location_id=self.kwargs['location_pk'])
    
    def perform_create(self, serializer):
        location = Location.objects.get(id=self.kwargs['location_pk'])
        serializer.save(location=location)