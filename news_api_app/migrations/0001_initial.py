# Generated by Django 3.0.6 on 2020-05-27 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
                ('added_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('state_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_api_app.State')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
