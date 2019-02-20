from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or request.user == obj.owner:
			return True
		return False