import pygame

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))

done = False

prevX = -1
prevY = -1
currX = -1
currY = -1

LMBPressed = False

color = 'red'

def its_color(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    return (0, 0, 0)

def draw_right_triangle(point1, point2, point3):
    pygame.draw.polygon(screen, its_color(color), [point1, point2, point3], 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBPressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.KEYDOWN:
            # determine if a letter key was pressed
            if event.key == pygame.K_r:
                color = 'red'
            elif event.key == pygame.K_g:
                color = 'green'
            elif event.key == pygame.K_b:
                color = 'blue'

        if event.type == pygame.MOUSEMOTION:
            if LMBPressed:
                currX = event.pos[0]
                currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBPressed = False
            baseLayer.blit(screen, (0, 0))
            currX = event.pos[0]
            currY = event.pos[1]
        
    if LMBPressed:
        screen.blit(baseLayer, (0, 0))
        draw_right_triangle((prevX, prevY), (prevX, currY), (currX, currY))

    pygame.display.flip()
