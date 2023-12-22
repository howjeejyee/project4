# Stick, League of Adventure

# Project Description
**Stick, League of Adventure** is a is a Turn-Based RPG game that required player to choose their action and fight enemy to go on his adventure. Player will control one of the stickman to fight off enemy and kill the end game boss to win the game! Hope you are ready for this game, please click the [link](https://project4-stick-turn-base-rpg-a7fd73f05e83.herokuapp.com/) here to head on to the webpage.

# Technologies Used

* Python
* Pygame
* Django
* HTML
* CSS
* Adobe Photoshop

# Guidelines
In **Stick, League of Adventure**, player must signup an account to login on the website before they can start the game. Player then should create their character after login and click on the Start Game button to startup the game. In the game, player can use their mouse to select which enemy to attack, the number that show on screen indicates different meaning. Red colour number means damage taken, where else green colour number means healing. Player will have 3 potions to heal them back to continue the fight. The objectives of this game is to kill the enemies. Below are some codes that used in this project.

This below code use **'Sprite'**. A Sprite is a fundamental class that represents game objects. It's a way to organize and manage graphical elements efficiently where including features such as grouping, image handling and others.
```python
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
```

This below code is part of the setup for pygame. This part is more towards drawing out the image and show it on pygame.
```python
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
       
       if warrior.is_visible():
          warrior.draw()

       for enemies in enemy:
          if enemies.is_visible():
            enemies.draw()
```
# Screenshots
Home Page
![Homepage image](/main_app/public/home.png)

Login Page
![Login image](/main_app/public/login.png)

After Login
![Start image](/main_app/public/start.png)

Game Images
![Game Image](/main_app/public/game1.png)

![Battle Image](/main_app/public/game2.png)

![Heal Image](/main_app/public/game3.png)

![Kill Image](/main_app/public/game4.png)

![Victory Image](/main_app/public/game5.png)

![Defeat Image](/main_app/public/game6.png)

# Future Plans
This game is far away from finish. There are a few ideas that can be implement into what can be done to improve the gameplay.
1. Adding storyline into the game and pop out the battle screen based on player decision
2. Adding new character and enemy 
3. Adding leveling system
4. Linking Django Database character creation with the game