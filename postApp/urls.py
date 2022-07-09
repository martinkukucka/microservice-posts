from django.urls import path
from postApp import views

urlpatterns = [
    path('posts/', views.post_list),
]