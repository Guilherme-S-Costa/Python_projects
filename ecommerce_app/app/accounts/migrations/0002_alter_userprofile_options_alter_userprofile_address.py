# Generated by Django 4.2 on 2023-04-22 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Perfil de usuário', 'verbose_name_plural': 'Perfis de usuários'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.JSONField(blank=True, verbose_name='Endereço'),
        ),
    ]
