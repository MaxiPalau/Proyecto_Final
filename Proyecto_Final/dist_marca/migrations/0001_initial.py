# Generated by Django 4.0.4 on 2022-07-03 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marcas', '0001_initial'),
        ('distribuidores', '0002_delete_distribuidores_marcas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidores_marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombre', to='distribuidores.distribuidores')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombre_marca', to='marcas.marcas')),
            ],
            options={
                'verbose_name': 'Distribuidores x marca',
                'verbose_name_plural': 'Distribuidores x marcas',
            },
        ),
    ]