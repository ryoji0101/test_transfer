# Generated by Django 4.2.3 on 2023-10-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0027_adcampaigns_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adcampaigns',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]