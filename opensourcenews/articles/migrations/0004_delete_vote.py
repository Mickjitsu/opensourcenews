# Generated by Django 4.2.16 on 2024-12-08 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_image_alter_article_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
