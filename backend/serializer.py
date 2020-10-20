from rest_framework import serializers
from .models import Post, Comment

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