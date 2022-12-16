from django.contrib import admin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from rest_framework_api_key.models import APIKey
from lands.views import LandViewSet, index

router = DefaultRouter()
router.register(r'lands', LandViewSet)


@csrf_exempt
def create_key(request, n):
    if request.method == 'POST':
        api_key, key = APIKey.objects.create_key(name=n)
        return JsonResponse({'key': key})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api-key/<n>/', create_key),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
