from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Character
from .forms import CharacterCreationForm
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
def select_character(request):
    characters = Character.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = CharacterCreationForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            return redirect('select_character')
    else:
        form = CharacterCreationForm()

    return render(request, 'start.html', {'form': form, 'characters': characters})

@login_required
def start(request):
    if request.method == 'POST':
        form = CharacterCreationForm(request.POST)
        if form.is_valid():
            # Associate the character with the current user
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            return redirect('start')  # Redirect to the same page after form submission

    else:
        form = CharacterCreationForm()

    characters = Character.objects.filter(user=request.user)
    return render(request, 'start.html', {'form': form, 'characters': characters})

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