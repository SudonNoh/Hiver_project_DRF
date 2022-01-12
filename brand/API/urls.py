from django.urls import path, include

from .views import BrandRetrieveUpdateAPIView

urlpatterns = [
    path('information', BrandRetrieveUpdateAPIView.as_view()),
]