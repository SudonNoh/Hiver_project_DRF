from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AdminUserViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'', AdminUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]