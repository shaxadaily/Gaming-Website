# Generated by Django 4.2.2 on 2023-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_genre_options_alter_game_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='store.genre', verbose_name='Жанры'),
        ),
    ]