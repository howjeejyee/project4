import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

game_panel = 200
screen_width = 800
screen_height = 400 + game_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

background_image = pygame.image.load('img/background.jpg').convert_alpha()
panel_image = pygame.image.load('img/gamepanel.jpg').convert_alpha()

def background():
  screen.blit(background_image, (50, 0))

def gamepanel():
  screen.blit(panel_image, (50, screen_height - game_panel))
  
run = True
while run:

  clock.tick(fps)
  background()
  gamepanel()
  
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False

  pygame.display.update()

pygame.quit()