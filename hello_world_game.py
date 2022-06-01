import pygame, pygame.locals, sys

pygame.init()

# Setup the window
window = pygame.display.set_mode((600, 600), 0, 64)
pygame.display.set_caption("Hello World Game - Alessandro")

# Global state variable
Quit = False


def process_events():
    global Quit
    # process all the events generated by the system
    for event in pygame.event.get():
        # event QUIT is generated when the user closes the application window
        if event.type == pygame.locals.QUIT:
            Quit = True


def update_game_logic():
    # do nothing at this moment
    return


def render():
    # clear the screen
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    window.fill(BLACK)

    # Print hello world
    font = pygame.font.SysFont(None, 48)
    text = font.render('Hello Alessandro', True, WHITE)
    textRect = text.get_rect()
    textRect.centerx = window.get_rect().centerx
    textRect.centery = window.get_rect().centery
    window.blit(text, textRect)

    # Update the display with the new content of the window
    pygame.display.update()


# Game loop
while not Quit:
    process_events()
    update_game_logic()
    render()

pygame.quit()
sys.exit()