# Generated by Django 4.2.3 on 2023-10-11 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_alter_notification_content2_alter_notification_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freezenotification',
            name='poster',
        ),
        migrations.AddField(
            model_name='freezenotification',
            name='poster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ice_alerts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
