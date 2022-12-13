from rest_framework import serializers

from lands.models import Land, PlotSize


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'

    plot_sizes = serializers.StringRelatedField(many=True)
    fees = serializers.StringRelatedField(many=True)
    images = serializers.StringRelatedField(many=True)
    landmarks = serializers.StringRelatedField(many=True)
    estate_features = serializers.StringRelatedField(many=True)
