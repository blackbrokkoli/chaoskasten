# Generated by Django 2.2.7 on 2021-03-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_profile_payment_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='free_account',
            field=models.BooleanField(default=False),
        ),
    ]
