# Generated by Django 4.2.3 on 2023-09-28 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0050_posts_qp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='views_count',
        ),
    ]