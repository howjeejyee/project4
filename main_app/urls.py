from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('start/', views.start, name='start'),
    path('start_game/', views.start_game, name='start_game'),
    path('accounts/signup/', views.signup, name='signup'),
    path('select_character/', views.select_character, name='select_character'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)