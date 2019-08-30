from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from users import views

schema_view = get_schema_view(
    openapi.Info(
        title="Test case API",
        default_version='v1',
        description="Just for test",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="porosya@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", views.HelloView.as_view(), name="hello"),
    path('api/users/', include('users.urls'), ),
    path('api/posts/', include('posts.urls'), ),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
]
