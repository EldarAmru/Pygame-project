import pygame
import button
from gameplay import play
from gameplay2 import play2
from gameplay3 import play3


def lvlmenu(run):
  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 600

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Выбор уровня")

  menu_state = "main"

  lvl1 = pygame.image.load("1level.png").convert_alpha()
  lvl2 = pygame.image.load("2level.png").convert_alpha()
  lvl3 = pygame.image.load("3level.png").convert_alpha()
  button1 = button.Button(304, 125, lvl1, 1)
  button2 = button.Button(304, 275, lvl2, 1)
  button3 = button.Button(304, 425, lvl3, 1)

  def load_image(name, colorkey=None):
      fullname = pygame.image.load(name)
      return fullname

  sprite = pygame.sprite.Sprite()
  sprite.image = load_image("arrow.png")
  sprite.rect = sprite.image.get_rect()
  all_sprites = pygame.sprite.Group(sprite)

  while run:

    screen.fill((52, 78, 91))

    if menu_state == "main":
      if button1.draw(screen):
        play()
      if button2.draw(screen):
        play2()
      if button3.draw(screen):
        play3()


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEMOTION:
        sprite.rect.x = event.pos[0]
        sprite.rect.y = event.pos[1]
    if pygame.mouse.get_focused():
      pygame.mouse.set_visible(False)
      all_sprites.draw(screen)

    pygame.display.update()

