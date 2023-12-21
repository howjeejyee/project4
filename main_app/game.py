import pygame
from django.shortcuts import render

def run_game(request):
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60
    
    game_panel = 200
    screen_width = 800
    screen_height = 400 + game_panel

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Stick, League of Adventure')
                               
    background_image = pygame.image.load('main_app/static/image/background.jpg').convert_alpha()
    panel_image = pygame.image.load('main_app/static/image/gamepanel.jpg').convert_alpha()

    def background():
       screen.blit(background_image, (0,0))
    
    def gamepanel():
        screen.blit(panel_image, (0, screen_height - game_panel + 80))

    run = True
    while run:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             run = False

       clock.tick(fps)
       background()
       gamepanel()

       pygame.display.update()

    pygame.quit()

    return render(request, 'start.html')