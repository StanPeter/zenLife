from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment

# Serializers define the API representation.


# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# Post Serializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# Comment Serializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# class MatchDetailSerializer(serializers.ModelSerializer):
#     sport = SportSerializer()
#     market = MarketSerializer()
#
#     class Meta:
#         model = Match
#         fields = ('id', 'url', 'name', 'startTime', 'sport', 'market')
