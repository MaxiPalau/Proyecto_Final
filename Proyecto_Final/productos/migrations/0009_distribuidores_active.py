# Generated by Django 4.0.4 on 2022-06-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_marcas_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribuidores',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
