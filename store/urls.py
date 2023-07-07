from django.urls import path
from .views import *
# app_name = 'game'

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop_page, name='shop_page'),
    path('shop/genre/<int:pk>', genre_page, name='genre_page'),
    path('product-details/<int:pk>', product_details_page, name='product_details_page'),
    path('add_game/', add_game, name='add_game'),
    path('add_genre/', add_genre, name='add_genre'),
    # path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/<int:pk>', profile, name='profile'),
    path('checkout/', button_to_buy, name='checkout'),
    path('success/', success_url, name='success'),

    path('delete/<int:pk>/', delete_game, name='delete_game'),
    path('update/<int:pk>', update_form, name='update_form')
]






