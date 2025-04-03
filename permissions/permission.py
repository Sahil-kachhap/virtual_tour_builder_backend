from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'ADMIN'

class IsEditorUser(permissions.BasePermission):
    """
    Allows access only to editor users or admins.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role in ['ADMIN', 'EDITOR']

class IsAdminOrSelf(permissions.BasePermission):
    """
    Allow users to edit their own profiles, but only admins can edit other profiles.
    """
    def has_object_permission(self, request, view, obj):
        return request.user and (request.user.role == 'ADMIN' or obj == request.user)

class IsAdminOrEditor(permissions.BasePermission):
    """
    Allow editors to edit their own content, but only admins can edit all content.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.role in ['ADMIN', 'EDITOR']
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and (request.user.role == 'ADMIN' or 
                               (request.user.role == 'EDITOR' and obj.created_by == request.user))

# permissions/apps.py
from django.apps import AppConfig

class PermissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'permissions'