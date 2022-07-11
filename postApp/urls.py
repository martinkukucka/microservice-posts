from django.urls import path
from postApp import views

"""
URL patterns
posts/ - all posts
posts/postId - post with selected id
posts/userId - all posts of selected user
"""
urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:postId>/', views.post_detail),
    path('users/<int:userId>/', views.posts_by_user),
]