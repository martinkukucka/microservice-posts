from rest_framework import serializers

from postApp.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')


class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')