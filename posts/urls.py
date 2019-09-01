from rest_framework.routers import DefaultRouter
from .viewsets import PostViewSet

router = DefaultRouter()
router.register(r'', PostViewSet, basename="posts")

app_name = 'posts'
urlpatterns = router.urls
