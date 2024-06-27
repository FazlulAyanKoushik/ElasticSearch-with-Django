from django.urls import path

from product.views import (
    ProductViewSet,
    ProductDocumentViewSet
)

urlpatterns = [
    path('search/', ProductDocumentViewSet.as_view(), name='product-search'),
    path("", ProductViewSet.as_view({'get': 'list'}), name="product-list"),
]