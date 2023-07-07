from django.contrib import admin
from .models import Genre, Game, Profile
# Register your models here


admin.site.register(Profile)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ['title']}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}