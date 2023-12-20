from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('gamestart/', views.start, name='start'),
    path('character/create/', views.character, name='character_create'),
    path('start_game/', views.start_game, name='start_game'),
    path('accounts/signup/', views.signup, name='signup')
]