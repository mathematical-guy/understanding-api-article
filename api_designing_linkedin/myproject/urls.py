from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from myapp.views import ProductViewSet, OrderViewSet

router = DefaultRouter()

router.register("products", ProductViewSet)
router.register("orders", OrderViewSet)


urls = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]


