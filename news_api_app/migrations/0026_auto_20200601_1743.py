# Generated by Django 3.0.6 on 2020-06-01 12:13

from django.db import migrations, models
import news_api_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0025_auto_20200601_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companines',
            name='newsDate',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[news_api_app.models.date_validate]),
        ),
        migrations.AlterField(
            model_name='companines',
            name='pdfUlr',
            field=models.FileField(blank=True, null=True, upload_to='CompanyPDFs/%Y/%m/%d'),
        ),
    ]
