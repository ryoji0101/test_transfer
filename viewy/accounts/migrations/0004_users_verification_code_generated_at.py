# Generated by Django 4.2.3 on 2023-07-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_users_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='verification_code_generated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
