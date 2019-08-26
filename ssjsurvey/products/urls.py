from django.urls import path, include
from . import views
from rest_framework import routers


router2 = routers.DefaultRouter()
router2.register('products', views.ProductsView)
urlpatterns = [
    path('', include(router2.urls)),
]
