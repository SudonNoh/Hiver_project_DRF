from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AdminBrandViewSet, AdminUserViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'user', AdminUserViewSet)
router.register(r'brand', AdminBrandViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]