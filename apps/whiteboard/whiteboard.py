import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
(screen_width, screen_height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

lines = []
lineColors = []

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colorList = [black, red, green, blue]
currentColor = black

drawing = False
drawingModeChanged = False

lastMovementTime = pygame.time.get_ticks()
lastMousePos = (0, 0)
minMouseMovement = 10

pygame.mouse.get_rel()

font = pygame.font.SysFont("arial", 72)
text = font.render("Not Drawing", True, (0, 128, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    screen.fill(white)
    screen.blit(text, (0, 0, text.get_width(), text.get_height()))

    for col in colorList:
        colorRect = (screen_width - (screen_height / len(colorList)), screen_height / len(colorList) * colorList.index(col), (screen_height / len(colorList)), (screen_height / len(colorList)))
        pygame.draw.rect(screen, col, colorRect)

    if abs(pygame.mouse.get_rel()[0]) >= minMouseMovement or abs(pygame.mouse.get_rel()[1]) >= minMouseMovement:
        lastMovementTime = pygame.time.get_ticks()
        drawingModeChanged = False

    if (not drawingModeChanged) and (pygame.time.get_ticks() - lastMovementTime >= 1000):
        if pygame.mouse.get_pos()[0] > screen_width - (screen_height / len(colorList)):
            currentColor = screen.get_at(pygame.mouse.get_pos())
        else:
            drawing = not drawing
            drawingModeChanged = True
            if drawing:
                text = font.render("Drawing ({}, {}, {})".format(currentColor[0], currentColor[1], currentColor[2]), True, (0, 128, 0))
                lines.append([])
                lineColors.append(currentColor)
            else:
                text = font.render("Not drawing", True, (0, 128, 0))

    if drawing:
        lines[-1].append(pygame.mouse.get_pos())

    for points in lines:
        lineColor = lineColors[lines.index(points)]
        if len(points) >= 2:
            pygame.draw.aalines(screen, lineColor, False, points)

    pygame.display.flip()