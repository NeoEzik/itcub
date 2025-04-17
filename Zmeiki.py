import pygame
import sys
import math
import random

pygame.init()

width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Солнечная система")

black = (0, 0, 0)
yellow = (255, 255, 0)
gray = (150, 150, 150)
orange = (255, 165, 0)
green = (0, 255, 0)
red = (255, 0, 0)
ponos = (189, 183, 107)
rizhiy = (255, 127, 80)
biruoviy = (0, 255, 255)
goluboi = (72, 209, 204)

sun_pos = (width // 2, height // 2)
planet_distances = [70, 100, 130, 160, 210, 270, 340, 390]
planet_colors = [gray, orange, green, red, ponos, rizhiy, biruoviy, goluboi]
planet_sizes = [8, 12, 12, 10, 25, 18, 18, 18]
planet_names = ["Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун"]
planet_angles = [0] * len(planet_distances)
rotation_speeds = [0.005, 0.004, 0.003, 0.002, 0.0015, 0.001, 0.0008, 0.0005]

font = pygame.font.Font(None, 36)


def draw_stars(num_stars):
    for _ in range(num_stars):
        x = random.randint(0, width)
        y = random.randint(0, height)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), random.randint(1, 3))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    draw_stars(100)  
    pygame.draw.circle(screen, yellow, sun_pos, 50)

    mouse_pos = pygame.mouse.get_pos()
    for i in range(len(planet_distances)):
        planet_angles[i] += rotation_speeds[i]
        x = sun_pos[0] + planet_distances[i] * math.cos(planet_angles[i])
        y = sun_pos[1] + planet_distances[i] * math.sin(planet_angles[i])
        pygame.draw.circle(screen, planet_colors[i], (int(x), int(y)), planet_sizes[i])


        if (int(x) - planet_sizes[i] < mouse_pos[0] < int(x) + planet_sizes[i] and
            int(y) - planet_sizes[i] < mouse_pos[1] < int(y) + planet_sizes[i]):
            text = font.render(planet_names[i], True, (255, 255, 255))
            screen.blit(text, (mouse_pos[0] + 10, mouse_pos[1] + 10))

    pygame.display.flip()
