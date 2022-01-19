from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SizeViewSet
    )


router = DefaultRouter(trailing_slash=False)
router.register(r'size', SizeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]