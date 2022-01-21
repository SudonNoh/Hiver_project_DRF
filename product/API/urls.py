from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SizeViewSet, ProductViewSet
    )


router = DefaultRouter(trailing_slash=False)
router.register(r'size', SizeViewSet)
router.register(r'items', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]