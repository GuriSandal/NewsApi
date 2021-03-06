# Generated by Django 3.0.6 on 2020-06-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0036_auto_20200609_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='imageUrl',
            field=models.ImageField(null=True, upload_to='CityNewsImages'),
        ),
        migrations.AlterField(
            model_name='companinespdf',
            name='imageUlr',
            field=models.ImageField(null=True, upload_to='MianNewsImages'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='imageUrl',
            field=models.ImageField(null=True, upload_to='MagazineImages'),
        ),
        migrations.AlterField(
            model_name='sundaymagazine',
            name='imageUrl',
            field=models.ImageField(null=True, upload_to='SundayMagazineImages'),
        ),
    ]
