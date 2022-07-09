# Create your views here.

import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from postApp.models import Post
from postApp.serializer import PostSerializer, PostByUserSerializer, PostEditSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def post_list(request):
    """
    List all posts, or create a new post.
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    """
    Retrieve, update or delete a post.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(pk))
            post = response.json()
            if len(post) > 0 and 'id' in post and 'userId' in post and 'title' in post and 'body' in post:
                Post(post['id'], post['userId'], post['title'], post['body']).save()
                post = Post.objects.get(pk=pk)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostEditSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def posts_by_user(request, pk):
    """
    Retrieve, delete all posts of chosen user.
    """
    try:
        post = Post.objects.filter(userId=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostByUserSerializer(post, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)