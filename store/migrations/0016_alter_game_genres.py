# Generated by Django 4.2.2 on 2023-06-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_game_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(related_name='game', to='store.genre', verbose_name='Жанры'),
        ),
    ]
