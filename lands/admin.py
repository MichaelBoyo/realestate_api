from django.contrib import admin
from lands.models import Land, Fee, PlotSize, Image, Landmark, EstateFeature

admin.site.register([Land, Fee, PlotSize, Image, Landmark, EstateFeature])
