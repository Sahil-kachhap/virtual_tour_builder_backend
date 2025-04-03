# virtual_tour_builder/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from users.views import UserViewSet
from tours.views import TourViewSet, TourImageViewSet
from locations.views import LocationViewSet, LocationMediaViewSet
from reviews.views import ReviewViewSet

# Root router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tours', TourViewSet, basename='tour')

# Tours nested router
tours_router = routers.NestedSimpleRouter(router, r'tours', lookup='tour')
tours_router.register(r'images', TourImageViewSet, basename='tour-images')
tours_router.register(r'locations', LocationViewSet, basename='tour-locations')
tours_router.register(r'reviews', ReviewViewSet, basename='tour-reviews')

# Locations nested router
locations_router = routers.NestedSimpleRouter(tours_router, r'locations', lookup='location')
locations_router.register(r'media', LocationMediaViewSet, basename='location-media')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(tours_router.urls)),
    path('', include(locations_router.urls)),
]
