from rest_framework import serializers
from .models import Location, LocationMedia
import requests
from django.conf import settings

class LocationMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationMedia
        fields = ('id', 'media_type', 'file', 'title', 'description')

class LocationSerializer(serializers.ModelSerializer):
    media = LocationMediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'latitude', 'longitude', 
                  'address', 'order', 'panorama_id', 'heading', 'pitch', 
                  'created_at', 'updated_at', 'media')
        read_only_fields = ('created_at', 'updated_at')
    
    def validate(self, attrs):
        # If no panorama_id is provided, try to fetch it from Google Street View API
        if not attrs.get('panorama_id') and attrs.get('latitude') and attrs.get('longitude'):
            try:
                api_key = settings.GOOGLE_STREET_VIEW_API_KEY
                if api_key:
                    lat = attrs['latitude']
                    lng = attrs['longitude']
                    url = f"https://maps.googleapis.com/maps/api/streetview/metadata?location={lat},{lng}&key={api_key}"
                    response = requests.get(url)
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('status') == 'OK':
                            attrs['panorama_id'] = data.get('pano_id')
            except Exception as e:
                # Just log the error, don't raise exception
                print(f"Error fetching panorama ID: {e}")
        
        return attrs
