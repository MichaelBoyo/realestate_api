from django.shortcuts import render
from rest_framework import viewsets

from lands.models import Land
from lands.serializers import LandSerializer


class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer


def index(request):
    return render(request, 'lands/index.html')