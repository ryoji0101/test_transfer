# Generated by Django 4.2.3 on 2023-09-24 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0012_remove_adcampaigns_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adcampaigns',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='adcampaigns',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
