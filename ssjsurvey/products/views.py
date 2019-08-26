from rest_framework import filters
from rest_framework import viewsets
from .models import Products
from products.serializers import ProductSerializer


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
