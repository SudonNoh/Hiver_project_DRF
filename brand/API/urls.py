from django.urls import path, include

from .views import BrandRetrieveUpdateAPIView

urlpatterns = [
    path('active', BrandRetrieveUpdateAPIView.as_view()),
]