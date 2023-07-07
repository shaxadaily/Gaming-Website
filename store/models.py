from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название жанра')
    slug = models.SlugField(unique=True, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre_page', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'



class Game(models.Model):
    title = models.CharField(max_length=255, default='Название', verbose_name='Название')
    description = models.TextField(default='Описание', verbose_name='Описание')

    poster = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Постер')
    # poster_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    # poster_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    slug = models.SlugField(unique=True, null=True)
    download = models.URLField(default='https://track.wg-aff.com/click?pid=700&offer_id=24', verbose_name='Ссылка на установку')
    video = models.URLField(null=True, blank=True, verbose_name='Видео(ссылка)')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')



    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
    def show_poster(self):
        return self.poster.url

    # def get_first_genre(self):
    #     return self.genres[0]

    def get_absolute_url(self):
        return reverse('product_details_page', kwargs={'pk': self.pk})

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    profile_bg = models.ImageField(upload_to='profile_bg', blank=True, null=True)
    bio = models.CharField(default='Обо мне', max_length=255, blank=True, null=True)
    subscription = models.BooleanField(default=False, blank=True, null=True, verbose_name='Подписка')
    def __str__(self):
        return self.user.username

    def get_profile_bg(self):
        try:
            return self.profile_bg.url
        except:
            return 'https://img.freepik.com/free-vector/space-game-background-neon-night-alien-landscape_107791-1624.jpg?w=2000&t=st=1687463187~exp=1687463787~hmac=b6c3f475e256c1ded59c1b1c1ad45e096958d61ba275b3dc3a326f90fc73a436'

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return 'https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI='

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


# class GameReview(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     review = models.TextField()
#     rating = models.IntegerField(choices=RATING, de)
