# Generated by Django 4.2.16 on 2024-12-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_is_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='relevant_quote',
            field=models.TextField(default='Example quote', max_length=50),
            preserve_default=False,
        ),
    ]