import pygame
import sys
import time
import math

pygame.init()

WIDTH, HEIGHT = 750, 750
WINDOW_SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Analog Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock_face_image = pygame.image.load("mickeyclock.jpeg").convert()  # Load clock face image

def draw_clock():
    window.fill(WHITE)

    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    minute_angle = (minute + second / 60) * 360 / 60
    second_angle = second * 360 / 60

    clock_face_rect = clock_face_image.get_rect(center=(WIDTH//2, HEIGHT//2))
    window.blit(clock_face_image, clock_face_rect)

    minute_length = 200
    minute_hand_x = WIDTH // 2 + minute_length * math.cos(math.radians(90 - minute_angle))
    minute_hand_y = HEIGHT // 2 - minute_length * math.sin(math.radians(90 - minute_angle))
    pygame.draw.line(window, BLACK, (WIDTH//2, HEIGHT//2), (minute_hand_x, minute_hand_y), 5)

    second_length = 240
    second_hand_x = WIDTH // 2 + second_length * math.cos(math.radians(90 - second_angle))
    second_hand_y = HEIGHT // 2 - second_length * math.sin(math.radians(90 - second_angle))
    pygame.draw.line(window, RED, (WIDTH//2, HEIGHT//2), (second_hand_x, second_hand_y), 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_clock()

    pygame.display.update()
    pygame.time.delay(1000)
