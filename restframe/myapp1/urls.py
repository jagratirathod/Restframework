from django.urls import path
from myapp1 import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# app_name = 'myapp1'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('mylogin/', views.mylogin.as_view()),
    path('login/', views.MyObtainTokenPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('Categorys/', views.Categorys.as_view(), name='category'),
    path('Categorys/<int:pk>/', views.Category_update.as_view(), name='category'),

    path('Restaurant/', views.Restaurant.as_view(), name='restaurant'),
    path('Restaurant/<int:pk>/', views.Restaurant_update.as_view(), name='restaurant'),
    path('Foods/', views.Foods.as_view(), name="foods"),
    path('wish/', views.MyWishlist.as_view()),
    path('addwish/<int:pk>/', views.AddInWishlist.as_view()),
    path('review/', views.ReviewProduct.as_view()),
    path('payment/', views.Payment.as_view()),    
    path('search/', views.SearchView.as_view()),    
    path('filter/<sort>', views.Filterby.as_view()),
    path('cart_add/<int:pk>/', views.cart_add.as_view(), name='cart_add'),




]
