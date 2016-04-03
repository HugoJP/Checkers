import pygame

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
