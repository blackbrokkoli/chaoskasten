# Generated by Django 2.2.7 on 2021-04-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210412_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='search_only_removed_from_learning',
            field=models.BooleanField(default=False),
        ),
    ]
