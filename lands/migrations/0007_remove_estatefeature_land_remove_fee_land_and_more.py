# Generated by Django 4.1.4 on 2022-12-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0006_remove_land_estate_features_estatefeature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estatefeature',
            name='land',
        ),
        migrations.RemoveField(
            model_name='fee',
            name='land',
        ),
        migrations.RemoveField(
            model_name='image',
            name='land',
        ),
        migrations.RemoveField(
            model_name='landmark',
            name='land',
        ),
        migrations.RemoveField(
            model_name='plotsize',
            name='land',
        ),
        migrations.AddField(
            model_name='land',
            name='estate_features',
            field=models.ManyToManyField(related_name='land_estate_features', to='lands.estatefeature'),
        ),
        migrations.AddField(
            model_name='land',
            name='fees',
            field=models.ManyToManyField(related_name='land_fees', to='lands.fee'),
        ),
        migrations.AddField(
            model_name='land',
            name='images',
            field=models.ManyToManyField(related_name='land_images', to='lands.image'),
        ),
        migrations.AddField(
            model_name='land',
            name='landmarks',
            field=models.ManyToManyField(related_name='land_landmarks', to='lands.landmark'),
        ),
        migrations.AddField(
            model_name='land',
            name='plot_sizes',
            field=models.ManyToManyField(related_name='land_plot_sizes', to='lands.plotsize'),
        ),
    ]
