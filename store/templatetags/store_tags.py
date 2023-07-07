from django.template import Library
from store.models import Game, Genre


register = Library()


@register.simple_tag()
def count_games(pk):
    genre = Genre.objects.get(pk=pk)
    games = Game.objects.filter(genres=genre)
    return games.count()


@register.simple_tag()
def count_all_games():
    return len(Game.objects.all())