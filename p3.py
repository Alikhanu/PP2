import pygame

#all defs:------------------------------------------------------------------------------------------
def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color_1 = (c1, c1, c2)
    elif color_mode == 'red':
        color_1 = (c2, c1, c1)
    elif color_mode == 'green':
        color_1 = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color_1, (x, y), width)

def set_color(color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    return color

def main():
    #Basa:----------------------------------------------------------------------------------------------
    WIDTH = 800
    HEIGHT = 480

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    baseLayer = pygame.Surface((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    prevX = -1
    prevY = -1
    currX = -1
    currY = -1

    radius = 15
    x = 0
    y = 0

    LMBPressed = False
    done = False

    mode = '0'
    color = 'blue'
    points = []

    #Code-----------------------------------------------------------------------------------------------
    while not done:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            #Quit
            if event.type == pygame.QUIT:
                done = True

            #mode and color
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_r:
                    color = 'red'
                elif event.key == pygame.K_g:
                    color = 'green'
                elif event.key == pygame.K_b:
                    color = 'blue'
                elif event.key == pygame.K_1:
                    mode = '1'
                elif event.key == pygame.K_2:
                    mode = '2'
                elif event.key == pygame.K_3:
                    mode = '3'
            
            #Rectangle
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mode == '2':
                print("LMB was clicked!")
                print(event.pos)
                LMBPressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]
                currX = event.pos[0]
                currY = event.pos[1]

            if event.type == pygame.MOUSEMOTION:
                if LMBPressed:
                    currX = event.pos[0]
                    currY = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mode == '2':
                print("LMB was released!")
                print(event.pos)
                LMBPressed = False
                baseLayer.blit(screen, (0, 0))
                currX = event.pos[0]
                currY = event.pos[1]

            
            #Draw
            if event.type == pygame.MOUSEBUTTONDOWN and mode == '1':
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and mode == '1':
                position = event.pos
                points = points + [position]
                points = points[-256:]
            
            '''if mode == '2':
                points = []'''

        
        '''if LMBPressed:
            screen.fill((0, 0, 0))
            screen.blit(baseLayer, (0, 0))
            pygame.draw.rect(screen, set_color(color), calculate_rect(prevX, currX, prevY, currY), 2)
'''
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)
        
main()