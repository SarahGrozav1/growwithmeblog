from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.HomeScreen.as_view(), name='home'),
    path('dashboard/', views.DashboardScreen.as_view(), name='dashboard'),
    path('dashboard/collaboration/', views.Collaboration, name='collaboration'),
    path('conclusion/', views.ConclusionScreen.as_view(), name='conclusion'),
    path('dashboard/about/', views.about_me, name='about'),
    path('Skincare/', views.PostList.as_view(), name='skincare'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]