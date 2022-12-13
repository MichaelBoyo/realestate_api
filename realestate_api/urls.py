from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from lands.views import LandViewSet

router = DefaultRouter()
router.register(r'lands', LandViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
