# Generated by Django 3.0.6 on 2020-05-29 12:43

from django.db import migrations, models
import news_api_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0020_magazine'),
    ]

    operations = [
        migrations.CreateModel(
            name='SundayMagazine',
            fields=[
                ('magazineId', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('magazineName', models.CharField(max_length=50)),
                ('fileName', models.FileField(upload_to='SundayMagazinePDFs/%Y/%m/%d')),
                ('imageUrl', models.ImageField(blank=True, null=True, upload_to='SundayMagazineImages/%Y/%m/%d')),
                ('newsDate', models.CharField(max_length=20, validators=[news_api_app.models.date_validate])),
                ('isActive', models.BooleanField(default=False)),
                ('addedOn', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Magazines',
            },
        ),
    ]
