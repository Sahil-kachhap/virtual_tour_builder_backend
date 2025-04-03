from rest_framework import serializers
from .models import Tour, TourImage
from locations.models import Location
from locations.serializers import LocationSerializer

class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = ('id', 'image', 'caption', 'order')

class TourSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True, read_only=True)
    locations = serializers.SerializerMethodField()
    created_by = serializers.ReadOnlyField(source='created_by.email')
    
    class Meta:
        model = Tour
        fields = ('id', 'title', 'slug', 'description', 'is_published', 
                 'created_by', 'created_at', 'updated_at', 'images', 'locations')
        read_only_fields = ('created_at', 'updated_at', 'slug')
    
    def get_locations(self, obj):
        locations = Location.objects.filter(tour=obj)
        return LocationSerializer(locations, many=True).data

class TourCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('title', 'description', 'is_published')
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)