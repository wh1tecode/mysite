# Generated by Django 4.2.11 on 2024-06-21 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_user_url_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_image',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='banner_image',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='url_address',
            field=models.CharField(default='2ab7b19a0bb143b086ed363550020e33', max_length=32),
        ),
    ]