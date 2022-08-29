from rest_framework.permissions import  BasePermission, SAFE_METHODS
from news.models import Item, Comment
class UpdateOrDelete(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or obj.created_with_api:
            return True
        return False