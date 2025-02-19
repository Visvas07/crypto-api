from rest_framework.permissions import BasePermission

class IsOrganizationOwner(BasePermission):
    """Custom permissions to allow only organization owner to edit or delete"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user