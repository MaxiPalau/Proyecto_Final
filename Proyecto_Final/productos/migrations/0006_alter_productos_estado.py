# Generated by Django 4.0.4 on 2022-06-26 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_alter_productos_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='productos.estados'),
        ),
    ]
