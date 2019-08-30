from django.contrib import admin
from django.urls import path
from users import views
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)


urlpatterns = [

    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router.urls)),
]

urlpatterns += router.urls
