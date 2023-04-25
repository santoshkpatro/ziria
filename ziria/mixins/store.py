from rest_framework.exceptions import APIException
from rest_framework import status

from ziria.models.store import Store


class StoreNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "store_not_found"
    default_detail = "Store Not Found"


class UnauthorizedStoreAccess(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = "unauthorized_store_access"
    default_detail = "Unauthorized store access"


class StoreInActiveException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = "inactive_store"
    default_detail = "Your store is inactive. Please contact our team for further help."


class StoreFetchMixin:
    def initial(self, request, *args, **kwargs):
        slug = kwargs.get("store_slug")
        try:
            store: Store = Store.objects.get(slug=slug)

            if not store.is_active:
                raise StoreInActiveException

            request.current_store = store
            super().initial(request, *args, **kwargs)
        except Store.DoesNotExist:
            raise StoreNotFoundException
