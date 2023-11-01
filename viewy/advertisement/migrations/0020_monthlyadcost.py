# Generated by Django 4.2.3 on 2023-10-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0019_setmeeting_address_setmeeting_company_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyAdCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_month', models.DateField(unique=True)),
                ('cpc', models.DecimalField(decimal_places=0, max_digits=4)),
                ('cpm', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
    ]