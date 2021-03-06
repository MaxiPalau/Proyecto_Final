# Generated by Django 4.0.4 on 2022-06-17 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribuidores_marcas',
            name='distribuidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombre', to='productos.distribuidores'),
        ),
        migrations.AlterField(
            model_name='distribuidores_marcas',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombre_marca', to='productos.marcas'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(default='', upload_to='prod_images'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='productos.marcas'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='productos.tipo'),
        ),
    ]
