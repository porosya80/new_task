from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", views.HelloView.as_view(), name="hello"),
    path('api/users/', include('users.urls') ),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
