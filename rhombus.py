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

def draw_rhombus(center_x, center_y, width, height):
    half_width = width / 2
    half_height = height / 2
    point1 = (center_x - half_width, center_y)
    point2 = (center_x, center_y - half_height)
    point3 = (center_x + half_width, center_y)
    point4 = (center_x, center_y + half_height)
    pygame.draw.polygon(screen, its_color(color), [point1, point2, point3, point4], 2)

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
        width = currX - prevX
        height = currY - prevY
        draw_rhombus((prevX + currX) / 2, (prevY + currY) / 2, abs(width), abs(height))

    pygame.display.flip()
