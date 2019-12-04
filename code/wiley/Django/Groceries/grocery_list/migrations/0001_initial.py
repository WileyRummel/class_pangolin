# Generated by Django 3.0 on 2019-12-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_description', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_completed', models.DateTimeField(verbose_name='date completed')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
