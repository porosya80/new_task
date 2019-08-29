from django.conf import settings
from django.db import models
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='author',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes")

    def __str__(self):
        return self.title

    # @property
    # def total_likes(self):
    #     return self.likes.count()
