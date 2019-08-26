from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


router3 = routers.DefaultRouter()
router3.register('survey', views.SurveyView)
urlpatterns = [
    path('', include(router3.urls)),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
