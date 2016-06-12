import pygame
import pygame.sprite

def Base(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()


def start_game():
    (width, height) = (512, 512)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Checkers")
    background_colour = (255, 255, 255)
    screen.fill(background_colour)
    bg = pygame.image.load("checkers.jpg")
    screen.blit(bg, (0, 0))

    pygame.display.flip()

    running = True
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    start_game()

