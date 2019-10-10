import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
lines = []
white = (255, 255, 255)
black = (0, 0, 0)
drawing = False
drawingModeChanged = False
lastMovementTime = pygame.time.get_ticks()
lastMousePos = (0, 0)
minMouseMovement = 10
pygame.mouse.get_rel()

font = pygame.font.SysFont("arial", 72)
text = font.render("Hello, World", True, (0, 128, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    screen.fill(white)
    screen.blit(text, (0, 0, text.get_width(), text.get_height()))

    if abs(pygame.mouse.get_rel()[0]) >= minMouseMovement or abs(pygame.mouse.get_rel()[1]) >= minMouseMovement:
        lastMovementTime = pygame.time.get_ticks()
        drawingModeChanged = False

    if (not drawingModeChanged) and (pygame.time.get_ticks() - lastMovementTime >= 1000):
        drawing = not drawing
        drawingModeChanged = True
        if drawing:
            text = font.render("Drawing", True, (0, 128, 0))
            lines.append([])
        else:
            text = font.render("Not drawing", True, (0, 128, 0))

    if drawing:
        lines[-1].append(pygame.mouse.get_pos())

    for points in lines:
        if len(points) >= 2:
            pygame.draw.aalines(screen, black, False, points)

    pygame.display.flip()