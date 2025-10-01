from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, CategoryViewSet, ProductViewSet
from . import views_templates

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Template views
    path('base/', views_templates.base, name='base'),
    path('', views_templates.buyer_home, name='buyer_home'),
    path('signup/', views_templates.signup_view, name='signup'),
    path('login/', views_templates.login_view, name='login'),
    path('logout/', views_templates.logout_view, name='logout'),
    path('seller/', views_templates.seller_home, name='seller_home'),
    path('product/<int:pk>/', views_templates.product_detail, name='product_detail'),
    path('seller/<int:pk>/', views_templates.seller_detail, name='seller_detail'),
    
    # API endpoints
    path('api/', include(router.urls)),
]
