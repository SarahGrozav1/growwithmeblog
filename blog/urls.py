from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeScreen.as_view(), name='home'),
    path('Skincare/', views.PostList.as_view(), name='skincare'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]