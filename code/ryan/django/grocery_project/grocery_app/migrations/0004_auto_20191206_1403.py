# Generated by Django 3.0 on 2019-12-06 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0003_groceryitem_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date completed'),
        ),
    ]
