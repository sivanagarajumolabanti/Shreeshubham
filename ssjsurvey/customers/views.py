import pdb

from rest_framework import filters, viewsets
from rest_framework.response import Response
from .models import Customer
from .serializers import MyordersSerializer, Wishlistorders
from customers.serializers import CustomerSerializer


class CustomerView(viewsets.ModelViewSet):
    # pdb.set_trace()
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('mobile',)


class MyordersView(viewsets.ModelViewSet):
    # pdb.set_trace()
    queryset = Customer.objects.all()
    serializer_class = MyordersSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id',)

    def retrieve(self, request, pk=None):
        # pdb.set_trace()
        queryset = Customer.objects.get(id=pk)
        serializer = MyordersSerializer(queryset, context={"product_type": request.query_params.get('product_type')})
        return Response(serializer.data)


class WishlistView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Wishlistorders
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id',)

    def retrieve(self, request, pk=None):
        pdb.set_trace()
        queryset = Customer.objects.get(id=pk)
        serializer = Wishlistorders(queryset)
        return Response(serializer.data)
