# Generated by Django 2.2.7 on 2021-03-05 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210305_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='stripeSubscriptionID',
        ),
    ]
