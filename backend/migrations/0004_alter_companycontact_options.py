# Generated by Django 5.2 on 2025-05-19 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_companycontact_alter_companyfundraiseterms_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companycontact',
            options={'ordering': ['-created_at'], 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
    ]
