import pygame

WIDTH = 800
HEIGHT = 480

prevX = -1
prevY = -1
currX = -1
currY = -1

LMBPressed = False
screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def main():
    pygame.init()
    global LMBPressed

    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = '0'
    color = 'blue'
    points = []
    done = False
    

    while not done:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                
                #mode and color
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
            
            #Draw
            if event.type == pygame.MOUSEBUTTONDOWN and mode == '1':
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and mode == '1':
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, color)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)         


main()