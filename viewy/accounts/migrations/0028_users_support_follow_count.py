# Generated by Django 4.2.3 on 2023-10-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_users_is_advertiser'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='support_follow_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]