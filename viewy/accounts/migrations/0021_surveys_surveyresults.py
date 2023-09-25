# Generated by Django 4.2.3 on 2023-09-25 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_users_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('options', models.ManyToManyField(to='accounts.features')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('selected_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.features')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.surveys')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'survey')},
            },
        ),
    ]
