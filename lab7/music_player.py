import pygame

pygame.init()

screen_width = 300
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sound Player")

WHITE = (255, 255, 255)

sound1 = pygame.mixer.Sound('sound1.mp3')
sound2 = pygame.mixer.Sound('sound2.mp3')
sound3 = pygame.mixer.Sound('sound3.mp3')
sounds = [sound1, sound2, sound3]
current_sound = 0

playing = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    sounds[current_sound].stop()
                    playing = False
                else:
                    sounds[current_sound].play()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current_sound = (current_sound + 1) % len(sounds)
                if playing:
                    sounds[current_sound].play()
            elif event.key == pygame.K_LEFT:
                current_sound = (current_sound - 1) % len(sounds)
                if playing:
                    sounds[current_sound].play()

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
