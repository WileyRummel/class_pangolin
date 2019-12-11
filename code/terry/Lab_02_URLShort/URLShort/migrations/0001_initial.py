# Generated by Django 3.0 on 2019-12-09 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputURL', models.CharField(max_length=64)),
                ('shortURL', models.CharField(max_length=12)),
                ('ip', models.CharField(max_length=16)),
                ('redirect', models.CharField(max_length=16)),
                ('url_bits', models.IntegerField(default=0)),
            ],
        ),
    ]
