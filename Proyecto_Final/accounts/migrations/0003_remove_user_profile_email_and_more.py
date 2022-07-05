# Generated by Django 4.0.4 on 2022-07-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='descripcion',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='link',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]
