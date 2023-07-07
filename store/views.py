from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Count
from .forms import GameForm, GenreForm, RegisterForm, LoginForm
from .models import Game, Genre, Profile
from django.contrib import messages
from gamestore import settings
import stripe
from django.urls import reverse


# Create your views here.
def index(request):
    games = Game.objects.all()
    genres = Genre.objects.all()
    game = Game.objects.filter().first()
    context = {
        'games': games[:4],
        'genres': genres,
        'game': game
    }
    return render(request, 'store/index.html', context)


def shop_page(request):
    games = Game.objects.all()
    genres = Genre.objects.all()
    context = {
        'games': games,
        'genres': genres,
    }

    return render(request, 'store/shop.html', context)


def genre_page(request, pk):
    genre = Genre.objects.get(pk=pk)
    games = Game.objects.filter(genres=genre)
    genres = Genre.objects.all()

    context = {
        'genres': genres,
        'games': games,
    }
    return render(request, 'store/shop.html', context)



def product_details_page(request, pk):
    game = Game.objects.get(pk=pk)
    genres = Genre.objects.filter(game=pk)[0]
    related_games = Game.objects.filter(genres=genres).exclude(pk=pk)[:5]
    profile = Profile.objects.get(pk=request.user.pk)

    context = {
        'game': game,
        'genres': genres,
        'related_games': related_games,
        'profile': profile
    }
    return render(request, 'store/product-details.html', context)


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            form.save_m2m()
            return redirect('shop_page')
    else:
        form = GameForm()

    context = {
        'form': form,
    }
    return render(request, 'store/add_game.html', context)


def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop_page')
    else:
        form = GenreForm()

    context = {
        'form': form,
    }
    return render(request, 'store/add_genre.html', context)


# Регистрация И Логин

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, 'Вы вошли в аккаунт!')
                return redirect('shop_page')
        else:
            messages.error(request, 'Неверные имя пользователя или пароль')
            return redirect('login')
    else:
        form = LoginForm()
    context = {
        'title': 'Логин',
        'form': form
    }
    return render(request, 'store/login.html', context)


def user_logout(request):
    logout(request)
    messages.warning(request, 'Вы вышли из аккаунта')
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('index')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('register')
    else:
        form = RegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'store/login.html', context)


def profile(request, pk):
    profile = Profile.objects.get(user_id=pk)

    context = {
        'profile': profile,
        'title': 'Страница пользователя'
    }
    return render(request, 'store/profile.html', context)


def button_to_buy(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=[
            'card',
        ],
        line_items=[
            {
                'price': 'price_1NRKLyCEyQ5qfpzozK7rlJkv',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success'))
    )
    return redirect(checkout_session.url, code=303)


def success_url(request):
    user = request.user.pk
    profile = Profile.objects.get(user_id=user)
    profile.subscription = True
    profile.save()
    messages.success(request, 'Оплата прошла успешно')
    return render(request, 'store/index.html')


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('shop_page')

    context = {
        'game': game,
        "asd": "aslkjdajdaskldjalksdjaskld"
    }
    return render(request, 'store/product-details.html', context)


def update_form(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            form.save_m2m()
            return redirect('product_details_page', pk)
    else:
        form = GameForm(instance=game)
    context = {
        'form': form,
        'game': game
    }
    return render(request, 'store/update_form.html', context)
