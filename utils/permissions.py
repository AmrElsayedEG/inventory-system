from rest_framework.permissions import BasePermission, IsAuthenticated
from .choices import UserTypeChoices

class IsManagerUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.type == UserTypeChoices.MANAGER)

class IsStockKeeperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.type == UserTypeChoices.STORE_KEEPER)

class IsRepresentitiveUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.type == UserTypeChoices.REPRESENTATIVE)

class ProductModifyUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.type == UserTypeChoices.MANAGER) or bool(request.user.type == UserTypeChoices.STORE_KEEPER)