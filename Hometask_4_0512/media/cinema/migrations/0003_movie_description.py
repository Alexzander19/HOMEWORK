# Generated by Django 5.1.4 on 2024-12-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default='Какое-то описани при создании поля после миграции'),
            preserve_default=False,
        ),
    ]