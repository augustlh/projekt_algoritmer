import pygame
import random
import math

pygame.init()

window_size = (800, 600)
window_title = "Visualisering af sorteringsalgoritmer"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)
clock = pygame.time.Clock()

n = 400
width = window_size[0] // n
arr = [random.randint(10, window_size[1] - 10) for _ in range(n)]

def visualize(arr : list[int], indices : list[int]) -> None:
    screen.fill((255, 255, 255))
    for i in range(len(arr)):
        color = (255, 0, 0) if i in indices else (0, 0, 0)
        rect = pygame.Rect(i * width, window_size[1] - arr[i], width, arr[i])
        pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
            


def selection_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        min_index = i

        for j in range(i + 1, len(temp)):
            if temp[j] < temp[min_index]:
                min_index = j

        temp[i], temp[min_index] = temp[min_index], temp[i];

        visualize(temp, [i, min_index])
        pygame.event.pump()
        clock.tick(60)

    return temp



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    arr = selection_sort(arr)

pygame.quit()