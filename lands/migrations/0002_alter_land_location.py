# Generated by Django 4.1.4 on 2022-12-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='location',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]