from django.urls import path
from postApp import views

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:pk>', views.post_detail),
    path('users/<int:pk>', views.posts_by_user),
]