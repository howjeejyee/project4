from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import pygame

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
    error_message = ''
    form = UserCreationForm(request.POST) 
    if request.method == 'POST': 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            return redirect('start') 
        else:
            error_message = 'Invalid sign up - try again'
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def character(request):
    return render(request, 'character.html')

@login_required
def start(request):
    return render(request, 'start.html')

def start_game(request):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Game')
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()

    return render(request, 'start.html')