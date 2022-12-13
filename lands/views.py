from rest_framework import viewsets

from lands.models import Land
from lands.serializers import LandSerializer


class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
