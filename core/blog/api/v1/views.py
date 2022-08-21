from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import *
from blog.models import *
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def list_api_view(request):
    if request.method == 'GET':
        post = Post.objects.filter(status=1)
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def detail_api_view(request,id):
    post = get_object_or_404(Post,pk=id,status=1)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'item removed'},status=status.HTTP_204_NO_CONTENT)