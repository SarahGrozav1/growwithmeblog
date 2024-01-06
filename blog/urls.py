from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.HomeScreen.as_view(), name='home'),
    path('dashboard/', views.DashboardScreen.as_view(), name='dashboard'),
    path('conclusion/', views.ConclusionScreen.as_view(), name='conclusion'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('Skincare/', views.PostList.as_view(), name='skincare'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]