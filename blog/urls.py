from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.HomeScreen.as_view(), name='home'),
    path('conclusion/', views.ConclusionScreen.as_view(), name='conclusion'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/collaboration/', views.Collaboration, name='collaboration'),
    path('dashboard/about/', views.about_me, name='about'),
    path('dashboard/books/', views.BooksScreen.as_view(), name='books'),
    path('dashboard/parenting/', views.ParentingScreen.as_view(), name='parenting'),
    path('dashboard/fashion/', views.FashionScreen.as_view(), name='fashion'),
    path('dashboard/skincare/', views.SkincareScreen.as_view(), name='skincare'),
    path('blog/<slug:slug>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
    path('blog/<slug:slug>/delete_comment/<int:comment_id>',views.comment_delete, name='comment_delete'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    
]