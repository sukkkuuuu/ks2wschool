# Generated by Django 4.1.3 on 2022-11-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='short_info',
            field=models.TextField(blank=True, max_length=128),
        ),
    ]
