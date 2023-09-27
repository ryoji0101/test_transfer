# Generated by Django 4.2.3 on 2023-09-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0041_merge_20230914_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='affiliate_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]