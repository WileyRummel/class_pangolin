# Generated by Django 3.0.2 on 2020-01-31 00:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=100, null='true')),
                ('venue', models.CharField(max_length=100, null='true')),
                ('street_address', models.CharField(max_length=100, null='true')),
                ('city', models.CharField(max_length=100, null='true')),
                ('state', models.CharField(max_length=100, null='true')),
                ('date', models.CharField(max_length=100, null='true')),
                ('time', models.CharField(max_length=100, null='true')),
                ('favorite', models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
