import pygame
import random

pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock to control the frame rate
clock = pygame.time.Clock()

import pygame
import random

pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock to control the frame rate
clock = pygame.time.Clock()

num_boxes = 10
box_width = WIDTH // num_boxes
boxes = [pygame.Rect(i * box_width, HEIGHT, box_width, random.randint(10, HEIGHT - 10)) for i in range(num_boxes)]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].height > arr[j + 1].height:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Visualize the swap by updating the position of boxes
                arr[j].x, arr[j + 1].x = arr[j + 1].x, arr[j].x

# Call the sorting function
bubble_sort(boxes)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    for box in boxes:
        pygame.draw.rect(screen, WHITE, box)

    pygame.display.flip()
    clock.tick(60)  # Control the frame rate

pygame.quit()
