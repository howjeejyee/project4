import pygame
import random
from .button import Button
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

    current_character = 1
    total_characters = 3
    action_cooldown = 0
    action_wait = 90
    attack = False
    potion = False
    potion_heal = 20
    click = False
    game_over = 0

    font = pygame.font.SysFont('Arial', 18)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
                               
    background_image = pygame.image.load('main_app/static/image/background.jpg').convert_alpha()
    panel_image = pygame.image.load('main_app/static/image/gamepanel.jpg').convert_alpha()
    mouse_image = pygame.image.load('main_app/static/image/mouse.png').convert_alpha()
    potion_image = pygame.image.load('main_app/static/image/potion.jpg').convert_alpha()


    def text(text, font, text_col, x, y):
       image = font.render(text, True, text_col)
       screen.blit(image, (x, y))


    def background():
        screen.blit(background_image, (0,0))
    
    def gamepanel():
        screen.blit(panel_image, (0, screen_height - game_panel + 80))
        text(f'{warrior.name} HP: {warrior.hp}', font, white, 80, screen_height - game_panel + 120)
        text(f'{soldier.name} HP: {soldier.hp}', font, black, 530, screen_height - game_panel + 95)
        text(f'{boss.name} HP: {boss.hp}', font, black, 525, screen_height - game_panel + 135)

    class character():
       def __init__(self, x, y, name, maxhp, str, potions):
          self.name = name
          self.maxhp = maxhp
          self.hp = maxhp
          self.str = str
          self.potions = potions
          self.alive = True
          image = pygame.image.load(f'main_app/static/image/{self.name}/char1.png')
          self.image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2))
          self.rect = self.image.get_rect()
          self.rect.center = (x, y)

       def attack(self, target):
          rdm = random.randint(-3, 3)
          damage = self.str + rdm
          target.hp -= damage

          if target.hp < 1:
             target.hp = 0
             target.alive = False

          damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
          damage_text_group.add(damage_text)

       def draw(self):
          screen.blit(self.image, self.rect)
   

    class HealthBar():
       def __init__(self, x, y, hp, maxhp):
          self.x = x
          self.y = y
          self.hp = hp
          self.maxhp = maxhp

         
       def draw(self, hp):
          self.hp = hp
          ratio = self.hp / self.maxhp
          pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
          pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))
   
    class DamageText(pygame.sprite.Sprite):
       def __init__(self, x, y, damage, colour):
          pygame.sprite.Sprite.__init__(self)
          self.image = font.render(damage, True, colour)
          self.rect = self.image.get_rect()
          self.rect.center = (x, y)
          self.counter = 0

       def update(self):
          self.rect.y -= 1
          self.counter += 1
          if self.counter > 30:
             self.kill()



    damage_text_group = pygame.sprite.Group()

    warrior = character(150, 370, 'Warrior', 35, 10, 3)
    soldier = character(500, 370, 'Soldier', 15, 5, 0)
    boss = character(650, 360, 'Captain', 50, 7, 0)

    enemy = []
    enemy.append(soldier)
    enemy.append(boss)

    warrior_healthbar = HealthBar(65, screen_height - game_panel + 145, warrior.hp, warrior.maxhp)
    soldier_healthbar = HealthBar(515, screen_height - game_panel + 115, soldier.hp, soldier.maxhp)
    boss_healthbar = HealthBar(515, screen_height - game_panel + 155, boss.hp, boss.maxhp)

    potion_button = Button(screen, 270, screen_height - game_panel + 112, potion_image, 64, 64)


    run = True
    while run:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             run = False
          if event.type == pygame.MOUSEBUTTONDOWN:
             click = True
          else:
             click = False

       clock.tick(fps)
       background()
       gamepanel()
       warrior_healthbar.draw(warrior.hp)
       soldier_healthbar.draw(soldier.hp)
       boss_healthbar.draw(boss.hp)
       warrior.draw()
       for enemies in enemy:
          enemies.draw()
      
       damage_text_group.update()
       damage_text_group.draw(screen)
       


       attack = False
       potion = False
       target = None
       pygame.mouse.set_visible(True)
       position = pygame.mouse.get_pos()
       for count, enemies in enumerate(enemy):
          if enemies.rect.collidepoint(position):
             pygame.mouse.set_visible(False)
             screen.blit(mouse_image, position)
             if click == True:
                attack = True
                target = enemy[count]
       if potion_button.draw():
          potion = True
       
       text(str(warrior.potions), font, black, 320, screen_height - game_panel + 110)
       if game_over == 0:
         if warrior.alive == True:
            if current_character == 1:
               action_cooldown += 1
               if action_cooldown >= action_wait:
                  if attack == True and target != None:
                     warrior.attack(target)
                     current_character += 1
                     action_cooldown = 0
                  
                  if potion == True:
                     if warrior.potions > 0:
                        if warrior.maxhp - warrior.hp > potion_heal:
                           heal = potion_heal
                        else:
                           heal = warrior.maxhp - warrior.hp
                        warrior.hp += heal
                        warrior.potions -= 1
                        damage_text = DamageText(warrior.rect.centerx, warrior.rect.y, str(heal), green)
                        damage_text_group.add(damage_text)
                        current_character += 1
                        action_cooldown = 0
         else:
            game_over = -1
                        
         
         for count, enemies in enumerate(enemy):
            if current_character == 2 + count:
               if enemies.alive == True:
                  action_cooldown += 1
                  if action_cooldown >= action_wait:
                     enemies.attack(warrior)
                     current_character += 1
                     action_cooldown = 0
               else:
                  current_character += 1

         if current_character > total_characters:
            current_character = 1

       alive_enemies = 0
       for enemies in enemy:
          if enemies.alive == True:
             alive_bandits += 1
       if alive_bandits == 0:
          game_over = 1

       pygame.display.update()

    pygame.quit()

    return render(request, 'start.html')