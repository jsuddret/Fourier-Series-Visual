import pygame
import random
import time
import os
import math


def cos(val):
    return math.cos(val)


def sin(val):
    return math.sin(val)


def inv_sin(val):
    return math.asin(val)


pi = math.pi


window_width = 1440
window_height = 960
fps = 60
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

dark_grey = (49, 51, 53)
yellow = (255, 255, 0)
turquoise = (63, 224, 208)
window.fill(dark_grey)

N = 1
t = 0
r = 0
theta = 0
x_initial = 420
y_initial = 540
fourier_list = []
line = 480

iterations = 1

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.display.set_caption("Visual Fourier Series")
font = pygame.font.Font(None, 24)
label = font.render(str(theta) + 'pi', True, yellow)
run = True

while run:
    clock.tick(fps)
    window.fill(dark_grey)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x_i = x_initial
    y_i = y_initial

    for i in range(iterations):
        x_im1 = x_i
        y_im1 = y_i

        N = i * 2 + 1
        r = 150 * (4 / (N * pi))
        x_i += int(r * cos(N * t))
        y_i += int(r * sin(N * t))

        pygame.draw.circle(window, turquoise, (x_im1, y_im1), int(r), 2)
        pygame.draw.line(window, turquoise, (x_im1, y_im1), (x_i, y_i), 3)
        pygame.draw.circle(window, yellow, (x_i, y_i), 5)

        if x_i <= 420:
            if y_i - y_initial >= 0:
                theta = pi - inv_sin((y_i - y_initial) / (150*(4 / pi)))
            else:
                theta = (3*pi)/2 - inv_sin((y_i - y_initial) / (150 * (4 / pi)))
        else:
            if y_i - y_initial >= 0:
                theta = inv_sin((y_i - y_initial) / (150 * (4 / pi)))
            else:
                theta = 2*pi - inv_sin((y_i - y_initial) / (150 * (4 / pi)))

        theta = round(theta/3, 3)

    fourier_list.insert(0, y_i)

    if len(fourier_list) > 2000:
        fourier_list.pop()

    pygame.draw.line(window, turquoise, (x_i, y_i), (x_initial + line, fourier_list[0]), 3)

    for i in range(len(fourier_list)):
        pygame.draw.circle(window, yellow, (i + x_initial + line, fourier_list[i]), 3)

    t += 0.01
    label = font.render(str(theta) + 'pi', True, yellow)
    window.blit(label, ((x_initial + (x_im1 - x_initial / 2)), y_initial + (y_im1 - y_im1)/2))
    pygame.display.update()

pygame.quit()
