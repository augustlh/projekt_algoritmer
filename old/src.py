import random
import pygame

# -- pygame stuff --
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Visualisering af sorteringsalgoritmer")
clock = pygame.time.Clock()

#Hvor mange bars?
n = 200
width = window_size[0] // n
arr = [random.randint(10, window_size[1] - 10) for _ in range(n)]

#arr = [random.randint(10,100) for _ in range(10)]


def bubble_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            yield temp


def selection_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        min_index = i

        for j in range(i + 1, len(temp)):
            if temp[j] < temp[min_index]:
                min_index = j

        temp[i], temp[min_index] = temp[min_index], temp[i];
        yield temp


def visualize(arr : list[float]) -> None:
    screen.fill((255,255,255))
    
    for i in range (len(arr)):
        rect = pygame.Rect(i * width, window_size[1] - arr[i], width, arr[i])
        pygame.draw.rect(screen, (0,0,0), rect)
    
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    for x in selection_sort(arr):
        visualize(x)
        pygame.event.pump()
        clock.tick(50)

pygame.quit()

print(arr)


