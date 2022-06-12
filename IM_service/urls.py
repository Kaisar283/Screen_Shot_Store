from django.urls import path
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('products', Suppliers_productsView)
from IM_service.views import Supplier_ProductView, Category_ProductsView

urlpatterns = [
    path('products/<int:supple_id>', Supplier_ProductView.as_view()),
    path('category/<int:cat_id>', Category_ProductsView.as_view()),
]