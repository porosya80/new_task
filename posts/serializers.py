from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

from .services import is_fan

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'text',
            'is_fan',
            'total_likes',
        )

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return is_fan(obj, user)


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    def get_full_name(self, obj):
        return obj.get_full_name()
