# Generated by Django 4.0.4 on 2022-06-26 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_distribuidores_marcas_distribuidor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='productos',
            name='estado',
            field=models.CharField(default='hola', max_length=200),
        ),
    ]
