from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", views.HelloView.as_view(), name="hello"),
    path('api/users/', include('users.urls'), ),
    path('api/posts/', include('posts.urls'), ),
]
