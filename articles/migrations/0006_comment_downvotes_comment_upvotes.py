# Generated by Django 4.2.16 on 2024-12-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
