# Generated by Django 4.2.16 on 2024-12-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_eventos_app', '0004_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imagem_capa',
            field=models.ImageField(blank=True, null=True, upload_to='eventos/capas/'),
        ),
    ]
