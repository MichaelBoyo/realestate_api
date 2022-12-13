# Generated by Django 4.1.4 on 2022-12-13 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0004_remove_land_image_url_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fees',
            new_name='Fee',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RemoveField(
            model_name='land',
            name='landmarks',
        ),
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landmark', models.CharField(max_length=225)),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lands.land')),
            ],
        ),
    ]
