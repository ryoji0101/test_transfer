# Generated by Django 4.2.3 on 2023-07-14 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_ad_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ad',
            new_name='Ads',
        ),
    ]