from rest_framework import generics
from ..models import Post
from .serializers import PostSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class PostListView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)


class PostDetailView(generics.RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)