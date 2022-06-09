from django.urls import path
from .views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter
router.register(r'products', ProductViewSet)


urlpatterns = [] + router.urls