# Generated by Django 3.0.6 on 2020-06-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0030_auto_20200606_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='companines',
            name='companyLogo',
            field=models.ImageField(blank=True, null=True, upload_to='CompanyLogo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='imageUrl',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='companines',
            name='imageUlr',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='sundaymagazine',
            name='imageUrl',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
