from django.db import models


class Fee(models.Model):
    survey = models.IntegerField()
    development = models.IntegerField()
    legal_document = models.IntegerField()

    def __str__(self):
        return "Survey ₦ {:,}".format(self.survey) + " - " + "Development ₦ {:,}".format(
            self.development) + " - " + "Legal Document ₦ {:,}".format(self.legal_document)


class Image(models.Model):
    image_url = models.URLField()

    def __str__(self):
        return self.image_url


class Landmark(models.Model):
    landmark = models.CharField(max_length=225)

    def __str__(self):
        return self.landmark


class PlotSize(models.Model):
    size = models.CharField(max_length=50)
    price_per_plot = models.IntegerField()

    def __str__(self):
        return self.size + " - " + "₦ {:,}".format(self.price_per_plot) + " per plot"


class EstateFeature(models.Model):
    estate_feature = models.CharField(max_length=225)

    def __str__(self):
        return self.estate_feature


class Land(models.Model):
    location = models.CharField(max_length=225, null=True, blank=True)
    total_plots = models.IntegerField()
    plots_sold = models.IntegerField()
    plots_available = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=225)
    initial_deposit = models.IntegerField()
    promo = models.CharField(max_length=225, null=True, blank=True)
    owner = models.CharField(max_length=225)
    plot_sizes = models.ManyToManyField(PlotSize, related_name='land_plot_sizes', blank=True)
    fees = models.ManyToManyField(Fee, related_name='land_fees',  blank=True)
    images = models.ManyToManyField(Image, related_name='land_images', blank=True)
    landmarks = models.ManyToManyField(Landmark, related_name='land_landmarks',  blank=True)
    estate_features = models.ManyToManyField(EstateFeature, related_name='land_estate_features', blank=True)

    def __str__(self):
        return self.description
