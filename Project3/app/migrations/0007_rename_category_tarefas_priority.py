# Generated by Django 4.2 on 2023-04-08 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_tarefas_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefas',
            old_name='category',
            new_name='priority',
        ),
    ]