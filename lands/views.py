from django.shortcuts import render
from rest_framework import viewsets

from lands.models import Land
from lands.serializers import LandSerializer
from rest_framework_api_key.permissions import HasAPIKey


class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [HasAPIKey]


def index(request):
    return render(request, 'lands/index.html')
