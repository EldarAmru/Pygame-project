import pygame
from results3 import results3


screen = pygame.display.set_mode((800, 600))

class Key():
    def __init__(self, screen, color1, center1, center2, r, k, key):
        self.screen = screen
        self.color1 = color1
        self.center1 = center1
        self.center2 = center2
        self.k = k
        self.r = r
        self.key = key
        self.rect = pygame.Rect(center1, center2, 50, 20)
        self.handled = False


keys = [
    Key(screen, (255, 0, 0), 100, 540, 50, 10, pygame.K_d),
    Key(screen, (0, 255, 0), 210, 540, 50, 10, pygame.K_f),
    Key(screen, (0, 0, 255), 320, 540, 50, 10, pygame.K_k),
    Key(screen, (255, 255, 0), 430, 540, 50, 10, pygame.K_l),

]

def load_image(name, colorkey=None):
    fullname = pygame.image.load(name)
    return fullname



def load(map):
    circles = []
    f = open(map)
    data = f.readlines()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                circles.append(pygame.Rect(keys[x].rect.centerx - 46, y * -300, 50, 25))
    return circles


def play3():
    pygame.display.set_caption("Третий уровень")
    map_rect = load("3lvl.txt")
    score = 0
    pygame.font.init()
    my_font = pygame.font.SysFont('arial', 30)


    clock = pygame.time.Clock()
    while True:
        clock.tick(280)
        screen.fill((52, 78, 91))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        k = pygame.key.get_pressed()
        for key in keys:
            if k[key.key]:
                pygame.draw.circle(screen, (255, 255, 255), (key.center1, key.center2), 50, 10)
                key.handled = False
            if not k[key.key]:
                pygame.draw.circle(screen, key.color1, (key.center1, key.center2), 50, 10)
                key.handled = True


        for rect in map_rect:
            pygame.draw.circle(screen, (255, 255, 255), (rect.x + 20, rect.y), 42)
            rect.y += 5
            for key in keys:
                if key.rect.colliderect(rect) and not key.handled:
                    map_rect.remove(rect)
                    score += 5
                    key.handled = True
                    break
            if rect.y == 600:
                map_rect.remove(rect)
        if len(map_rect) == 0:
            results3()
        text_surface = my_font.render(str(score), False, (255, 255, 255))
        screen.blit(text_surface, (665, 200))
        text_LLL = my_font.render("Очки:", False, (255, 255, 255))
        screen.blit(text_LLL, (600, 200))
        f = open('score.txt', 'w')
        f.write(str(score))


        pygame.draw.rect(screen, (0, 0, 0), (40, 480, 448, 120), 10)
        pygame.draw.rect(screen, (0, 0, 0), (40, 0, 10, 500))
        pygame.draw.rect(screen, (0, 0, 0), (150, 0, 10, 600))
        pygame.draw.rect(screen, (0, 0, 0), (260, 0, 10, 600))
        pygame.draw.rect(screen, (0, 0, 0), (370, 0, 10, 600))
        pygame.draw.rect(screen, (0, 0, 0), (480, 0, 10, 600))


        pygame.display.update()
