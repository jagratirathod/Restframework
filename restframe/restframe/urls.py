from django.contrib import admin
from django.db import router
from forviewset import views
from formodelview import views
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('student',views.StudentView,basename='student'),
# router.register('MyView', views.MyViewSet ,basename='myview')



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('myapp1/', include('myapp1.urls')),
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),

    # path('gettoken/',obtain_auth_token)
]
