# Generated by Django 4.0.4 on 2022-07-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_remove_productos_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribuidores_marcas',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
