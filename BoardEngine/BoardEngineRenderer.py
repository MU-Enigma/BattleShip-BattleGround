import pygame

pygame.init()
pygame.display.init()

#Window Control variables
window_size = [800, 600]
window_caption = "PygameTemplate"
FPS=75
BackgroundColorRGB = [20, 0, 0]

# Runtime Variables
running = True
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

#Control Variables
Board = []

def onClose():
    pass

def render():
    pass

def gameloop():
    global screen, running, clock
    pygame.display.set_caption(window_caption)
    while running:
        screen.fill(BackgroundColorRGB)
        render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                onClose()
        pygame.display.update()
        clock.tick(FPS)
    onClose()


gameloop()