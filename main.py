import pygame
from pygame.sprite import Sprite


class Base(Sprite):
    def __init__(self, color, width, location):
        super().__init__()
        self.image = pygame.Surface([width, width])
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, color, (50, 50), 49, 0)
        self.rect = self.image.get_rect()
        self.rect.topleft = location


def start_game():
    (width, height) = (512, 512)
    color_blue = 0, 0, 255
    color_red = 255, 0, 0
    blue_1 = Base(color_blue, 100, (152, 40))
    blue_2 = Base(color_blue, 100, (372, 40))
    red_1 = Base(color_red, 100, (42, 372))
    red_2 = Base(color_red, 100, (262, 372))
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Checkers")
    background_colour = (255, 255, 255)
    screen.fill(background_colour)
    bg = pygame.image.load("checkers.jpg")
    screen.blit(bg, (0, 0))
    screen.blit(blue_1.image, blue_1.rect)
    screen.blit(blue_2.image, blue_2.rect)
    screen.blit(red_1.image, red_1.rect)
    screen.blit(red_2.image, red_2.rect)

    pygame.display.flip()

    running = True
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    start_game()

