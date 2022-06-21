from django.urls import path, include

from IM_kassa.views import Product_ByIDView, Product_ByBarcodeView, KassaSaleAPICreate

urlpatterns = [
    path('byid/<int:prod_id>', Product_ByIDView.as_view()),
    path('bybarcode/<int:barcode>', Product_ByBarcodeView.as_view()),
    path('sale', KassaSaleAPICreate.as_view())
]
