# Generated by Django 3.0.6 on 2020-05-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0004_headline_statelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='stateList',
            field=models.ManyToManyField(to='news_api_app.State'),
        ),
    ]
