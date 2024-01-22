import pygame
import button


def results3():
  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 600
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Результаты")


  resume_img = pygame.image.load("restart.png").convert_alpha()
  options_img = pygame.image.load("menu.png").convert_alpha()
  resume_button = button.Button(104, 325, resume_img, 1)
  options_button = button.Button(104, 450, options_img, 1)

  f = open('score.txt', 'r')
  score = str(*f)

  f1 = open('bestresoult3.txt', 'a')
  f1.write('\n' + score)

  with open('bestresoult3.txt', 'r') as q:
    last_line = q.readlines()[-1]
  with open('bestresoult3.txt', 'r') as q1:
    last_line1 = q1.readlines()[-2]
  with open('bestresoult3.txt', 'r') as q2:
    last_line2 = q2.readlines()[-3]

  def load_image(name, colorkey=None):
      fullname = pygame.image.load(name)
      return fullname

  def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

  sprite = pygame.sprite.Sprite()
  sprite.image = load_image("arrow.png")
  sprite.rect = sprite.image.get_rect()
  all_sprites = pygame.sprite.Group(sprite)
  font = pygame.font.SysFont('Arial', 45)
  pygame.font.init()
  my_font = pygame.font.SysFont('arial', 40)

  run = True
  while run:

    screen.fill((52, 78, 91))

    if resume_button.draw(screen):
      restart()
    if options_button.draw(screen):
      menu()
    text_score = my_font.render("очки: ", False, (255, 255, 255))
    screen.blit(text_score, (120, 200))
    text_surface = my_font.render(str(score), False, (255, 255, 255))
    screen.blit(text_surface, (200, 200))
    text_surface = str(last_line)
    blit_text(screen, text_surface, (600, 300), font)
    text_surface = str(last_line1)
    blit_text(screen, text_surface, (600, 400), font)
    text_surface = str(last_line2)
    blit_text(screen, text_surface, (600, 500), font)
    text_surface = my_font.render("Последние результаты", False, (255, 255, 255))
    screen.blit(text_surface, (420, 200))
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

def menu():
    from main import main
    main()


def restart():
  from gameplay3 import play3
  play3()
