# Generated by Django 4.2.16 on 2024-12-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_headline',
            field=models.BooleanField(default=False),
        ),
    ]