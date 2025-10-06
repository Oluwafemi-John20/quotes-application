from django.urls import path
from .views import RegisterUserAPIView, LoginUserAPIView

urlpatterns = [
    path('', RegisterUserAPIView.as_view(), name='user-register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
]
