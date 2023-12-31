# Generated by Django 4.2.2 on 2023-06-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_game_image_1_alter_game_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 1(слайдер)'),
        ),
        migrations.AlterField(
            model_name='game',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 2(слайдер)'),
        ),
        migrations.AlterField(
            model_name='game',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 3(слайдер)'),
        ),
        migrations.AlterField(
            model_name='game',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 4(слайдер)'),
        ),
    ]
