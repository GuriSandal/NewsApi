# Generated by Django 3.0.6 on 2020-05-28 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='added_on',
            new_name='addedOn',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='image_url',
            new_name='imageUlr',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='name',
            new_name='stateName',
        ),
    ]
