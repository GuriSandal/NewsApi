# Generated by Django 3.0.6 on 2020-05-28 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0009_remove_headline_statelist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headline',
            old_name='status',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='status',
            new_name='isActive',
        ),
    ]
