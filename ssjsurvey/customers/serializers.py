import itertools
import operator

from .models import Customer, Products
from rest_framework import serializers
from products.serializers import ProductSerializer


def most_common(L):
    SL = sorted((x, i) for i, x in enumerate(L))
    groups = itertools.groupby(SL, key=operator.itemgetter(0))

    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        return count, -min_index

    return max(groups, key=_auxfun)[0]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class MyordersSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('products',)

    def get_products(self, obj):
        l = []
        products = obj.order_quantity.all()
        if self.context.get('product_type'):
            products = products.filter(products__product_type=self.context.get('product_type').capitalize())
        for dt in products:
            ord_data = ProductSerializer(dt.products).data
            ord_data['quantity'] = dt.order_quantity
            l.append(ord_data)
        return l


class Wishlistorders(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('products', )

    def get_products(self, obj):
        products = obj.order_quantity.all().values_list('products__code', flat=True)
        pd = most_common(products)
        prod = Products.objects.filter(code=pd)
        return ProductSerializer(prod, many=True).data
