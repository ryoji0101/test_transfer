# Generated by Django 4.2.3 on 2023-10-11 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0060_remove_posts_support_follow_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='caption',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]