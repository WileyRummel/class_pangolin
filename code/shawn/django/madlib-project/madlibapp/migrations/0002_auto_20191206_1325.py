# Generated by Django 3.0 on 2019-12-06 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madlibapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madlibword',
            name='word',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
