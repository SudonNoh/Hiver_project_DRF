from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import AdminBrandViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'', AdminBrandViewSet)

urlpatterns = [
    path('', include(router.urls)),
]