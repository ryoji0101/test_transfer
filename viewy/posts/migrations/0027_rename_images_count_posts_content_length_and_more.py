# Generated by Django 4.2.3 on 2023-09-11 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_viewdurations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='images_count',
            new_name='content_length',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='video_length',
        ),
    ]
