# Generated by Django 5.2.1 on 2025-05-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ramal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=50, unique=True)),
                ('nome_completo', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('anydesk', models.CharField(max_length=10)),
            ],
        ),
    ]
