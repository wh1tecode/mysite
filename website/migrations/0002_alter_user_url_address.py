# Generated by Django 4.2.11 on 2024-06-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='url_address',
            field=models.CharField(default='fbd0f7c354294842a7e8eaf04767f485', max_length=32),
        ),
    ]
