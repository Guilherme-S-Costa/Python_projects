# Generated by Django 4.2 on 2023-04-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_options_alter_userprofile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.JSONField(blank=True, null=True, verbose_name='Endereço'),
        ),
    ]