from .products.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register(r"products", ProductViewSet, basename="product")

urlpatterns = router.urls