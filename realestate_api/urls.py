from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from lands.views import LandViewSet, index

router = DefaultRouter()
router.register(r'lands', LandViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
