# Generated by Django 3.0.1 on 2020-01-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug_me_app', '0005_auto_20200128_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='file',
            field=models.FileField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
