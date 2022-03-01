from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to edit theit own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
