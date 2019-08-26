from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


router1 = routers.DefaultRouter()
router1.register('customers', views.CustomerView)
router2 = routers.DefaultRouter()
router2.register('myorders', views.MyordersView)
router3 = routers.DefaultRouter()
router3.register('wishlist', views.WishlistView)
urlpatterns = [
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
