# Generated by Django 4.2.2 on 2023-06-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_game_poster_height_alter_game_poster_width'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='poster_height',
        ),
        migrations.RemoveField(
            model_name='game',
            name='poster_width',
        ),
        migrations.AlterField(
            model_name='game',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Постер'),
        ),
    ]
