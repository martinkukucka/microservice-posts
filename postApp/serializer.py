from rest_framework import serializers

from postApp.models import Post

"""
Post serializer with all post fields, used in GET all posts and POST new post 
"""


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


"""
Post serializer without userId, used in GET posts by userId.
"""


class PostByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')


"""
Post serializer for PUT method, fields title and body are editable. 
"""


class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')
