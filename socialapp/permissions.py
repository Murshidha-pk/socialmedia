from rest_framework import permissions

class OwnerOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):

        return request.user == obj.owner
    
    
class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):

        if request.method in permissions.SAFE_METHODS:

            return True
        
        return request.user == obj.owner