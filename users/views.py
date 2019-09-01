from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, )
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(GenericViewSet,
                  CreateModelMixin,
                  ListModelMixin,):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello, World!"}
        return Response(content)
