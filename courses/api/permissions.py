from rest_framework.permissions import BasePermission



# class IsEnrolled(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.students.filter(id=request.user.id).exists()


class IsEnrolled(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj == request.user
        else:
            return False
   