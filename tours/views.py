from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import Tour, TourImage
from .serializers import TourSerializer, TourCreateSerializer, TourImageSerializer
from permissions.permission import IsAdminOrEditor
from reviews.models import Review

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'created_at', 'updated_at']
    lookup_field = 'slug'
    
    def get_queryset(self):
        queryset = Tour.objects.all()
        if not self.request.user.is_authenticated or self.request.user.role == 'VIEWER':
            queryset = queryset.filter(is_published=True)
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TourCreateSerializer
        return TourSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsAdminOrEditor]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, slug=None):
        tour = self.get_object()
        reviews = Review.objects.filter(tour=tour)
        
        average_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
        
        data = {
            'average_rating': average_rating,
            'review_count': reviews.count(),
        }
        return Response(data)
    
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_tours(self, request):
        tours = Tour.objects.filter(created_by=request.user)
        serializer = self.get_serializer(tours, many=True)
        return Response(serializer.data)

class TourImageViewSet(viewsets.ModelViewSet):
    serializer_class = TourImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrEditor]
    
    def get_queryset(self):
        return TourImage.objects.filter(tour__slug=self.kwargs['tour_slug'])
    
    def perform_create(self, serializer):
        tour = Tour.objects.get(slug=self.kwargs['tour_slug'])
        serializer.save(tour=tour)
