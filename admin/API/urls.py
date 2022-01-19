from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AdminBrandViewSet, 
    AdminUserViewSet, 
    AdminGroupViewSet,
    AdminCategoryViewSet,
    AdminSubCategoryViewSet
    )


router = DefaultRouter(trailing_slash=False)
router.register(r'user', AdminUserViewSet)
router.register(r'brand', AdminBrandViewSet)
router.register(r'group', AdminGroupViewSet)
router.register(r'category', AdminCategoryViewSet)
router.register(r'subcategory', AdminSubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]