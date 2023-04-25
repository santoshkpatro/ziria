from rest_framework.permissions import BasePermission
from ziria.models.store_member import StoreMember


class HasStorePermission(BasePermission):
    def has_permission(self, request, view):
        try:
            request.store_member = StoreMember.objects.get(
                store=request.current_store, user=request.user
            )
            return True
        except StoreMember.DoesNotExist:
            return False


class HasStoreOrderViewPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.store_member:
            return False

        store_member: StoreMember = request.store_member
        if store_member.role == StoreMember.Role.OWNER or store_member.role == StoreMember.Role.ADMIN:
            return True

        if StoreMember.Permission.ORDER_VIEW in store_member.staff_permissions:
            return True

        return False


class HasStoreOrderDeletePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.store_member:
            return False

        store_member: StoreMember = request.store_member
        if store_member.role == StoreMember.Role.OWNER or store_member.role == StoreMember.Role.ADMIN:
            return True

        if StoreMember.Permission.ORDER_DELETE in store_member.staff_permissions:
            return True

        return False