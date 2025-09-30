from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ListBlogsAPIView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', views.BlogDetailAPIView.as_view(), name='blog-detail')
]