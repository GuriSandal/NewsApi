# Generated by Django 3.0.6 on 2020-06-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0027_auto_20200604_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sundaymagazine',
            name='addedOn',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
