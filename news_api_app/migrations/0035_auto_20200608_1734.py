# Generated by Django 3.0.6 on 2020-06-08 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0034_remove_companinespdf_districtnames'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='stateId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_api_app.State'),
        ),
        migrations.AddField(
            model_name='companinespdf',
            name='stateId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_api_app.State'),
        ),
    ]
