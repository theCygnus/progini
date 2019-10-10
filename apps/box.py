import pygame
import numpy as np

FPS = 30.0    # frames per seconds
TFRAME = 1/FPS

# fonts = pygame.font.get_fonts()
# print(fonts)
pygame.display.init()
pygame.font.init()
list_modes = pygame.display.list_modes()
dim = list_modes[3]
screen = pygame.display.set_mode(dim)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
bg_color = (230, 30, 30)

nx = list_modes[3][1]
ny = list_modes[3][0]

verticalx = 10
horizontaly = 100
x = np.arange(0, nx)
y = np.arange(0, ny)
X, Y = np.meshgrid(x, y)
Z = X + Y
Z = 255*Z/Z.max()
surf = pygame.surfarray.make_surface(Z)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
        if event.type == pygame.QUIT:
            sys.exit()

    # moving box (follows the finger)
    (xpos, ypos) = pygame.mouse.get_pos()
    boxw = 60
    boxh = 60
    allblack = np.zeros((ny, nx))
    allblack[xpos: xpos + boxw, ypos: ypos + boxh] = 20
    black = pygame.surfarray.make_surface(allblack)

    # Redraw the screen during each pass through the loop.
    screen.fill(bg_color)
    screen.blit(surf, (0, 0))
    screen.blit(black, (0, 0))
    clk = clock.get_fps()
    if clk == 0.0:
        t_frame = 0
    else:
        t_frame = 1/clk
        
    fps_str = "{0:.2f}".format(round(clk, 2))
    fps = font.render(fps_str + " fps", True, pygame.Color('white'))
    tsec_str = "{0:.2f}".format(round(t_frame*1000, 2))
    tsec = font.render(tsec_str + " ms", True, pygame.Color('white'))
    mouse = font.render("x:" + str(xpos) + " y:" + str(ypos), True, pygame.Color('white'))
    screen.blit(fps, (50, 50))
    screen.blit(tsec, (50, 100))
    screen.blit(mouse, (50, 150))
    clock.tick(FPS)

    # Make the most recently drown screen visible.
    pygame.display.flip()
