# Generated by Django 4.2.3 on 2023-09-27 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_users_is_specialadvertiser'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_advertiser',
            field=models.BooleanField(default=False),
        ),
    ]
