# Generated by Django 4.2.11 on 2024-05-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_about_created_date_about_updated_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=40)),
                ('message', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
    ]