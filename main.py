import pygame
import button
from lvlmenu import lvlmenu
from options import optionss


def main():
  pygame.init()

  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 600

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Меню")


  play_img = pygame.image.load("button_play.png").convert_alpha()
  options_img = pygame.image.load("button_options.png").convert_alpha()
  play_button = button.Button(304, 125, play_img, 1)
  options_button = button.Button(297, 250, options_img, 1)


  circle1 = pygame.image.load('circle.png')
  circle2 = pygame.transform.scale(circle1, (820, 620))
  circle11 = circle2.get_rect()

  def load_image(name, colorkey=None):
      fullname = pygame.image.load(name)
      return fullname

  sprite = pygame.sprite.Sprite()
  sprite.image = load_image("arrow.png")
  sprite.rect = sprite.image.get_rect()
  all_sprites = pygame.sprite.Group(sprite)

  run = True
  while run:

    screen.fill((52, 78, 91))

    if play_button.draw(screen):
      lvlmenu(run)
    if options_button.draw(screen):
      optionss()
    screen.blit(circle2, circle11)

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

  pygame.quit()

main()
