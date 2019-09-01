from .mixins import LikedMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostViewSet(LikedMixin,
                  CreateModelMixin,
                  ListModelMixin,
                  RetrieveModelMixin,
                  GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
