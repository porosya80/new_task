from django.contrib import admin
from django.urls import path
from users import views
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet

router = routers.SimpleRouter()
router.register(r'', UserViewSet,  basename='users')

app_name = 'users'
urlpatterns = [

    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(),
         name='token_verify'),
    path('', include(router.urls)),
]

# urlpatterns += router.urls