from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gamestart/', views.start, name='start'),
    path('character/create/', views.character, name='character_create'),
    path('start_game/', views.start_game, name='start_game'),
    path('accounts/signup/', views.signup, name='signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)