from django.urls import path, include
from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('current', UserRetrieveUpdateAPIView.as_view()),
]