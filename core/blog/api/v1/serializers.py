from rest_framework import serializers
from blog.models import *

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     id = serializers.IntegerField()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author','title','content','published_date','category']