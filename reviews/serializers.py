from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    user_name = serializers.ReadOnlyField(source='user.full_name')
    
    class Meta:
        model = Review
        fields = ('id', 'tour', 'user', 'user_name', 'rating', 'comment', 'created_at', 'updated_at')
        read_only_fields = ('user', 'user_name', 'created_at', 'updated_at')