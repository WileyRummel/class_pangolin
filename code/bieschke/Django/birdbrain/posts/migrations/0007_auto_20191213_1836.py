# Generated by Django 3.0 on 2019-12-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_peekchure'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Peekchure',
        ),
        migrations.AddField(
            model_name='post',
            name='peekchure',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='brain',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
