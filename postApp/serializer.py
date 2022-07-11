from rest_framework import serializers

from postApp.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer with all post fields, used in GET all posts and POST new post
    """

    class Meta:
        model = Post
        fields = '__all__'


class PostByUserSerializer(serializers.ModelSerializer):
    """
    Post serializer without userId, used in GET posts by userId.
    """

    class Meta:
        model = Post
        fields = ('id', 'title', 'body')


class PostEditSerializer(serializers.ModelSerializer):
    """
    Post serializer for PUT method, fields title and body are editable.
    """

    class Meta:
        model = Post
        fields = ('title', 'body')
