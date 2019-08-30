from django.conf import settings
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from users.models import User


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='author',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
