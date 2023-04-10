# Generated by Django 4.2 on 2023-04-10 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_tasks_content_alter_tasks_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[('alto', 'Alto'), ('medio', 'Médio'), ('baixo', 'Baixo')], default='important', max_length=100, verbose_name='Importante'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('concluido', 'Concluído'), ('Pendente', 'Pendente'), ('adiado', 'Adiado')], default='pending', max_length=100, verbose_name='Pendente'),
        ),
    ]
