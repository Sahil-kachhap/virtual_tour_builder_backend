# reviews/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from tours.models import Tour

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsReviewOwner]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        return Review.objects.filter(tour__slug=self.kwargs['tour_slug'])
    
    def perform_create(self, serializer):
        tour = Tour.objects.get(slug=self.kwargs['tour_slug'])
        serializer.save(user=self.request.user, tour=tour)
    
    def create(self, request, *args, **kwargs):
        tour = Tour.objects.get(slug=self.kwargs['tour_slug'])
        # Check if the user has already reviewed this tour
        if Review.objects.filter(user=request.user, tour=tour).exists():
            return Response(
                {"detail": "You have already reviewed this tour."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)

class IsReviewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user