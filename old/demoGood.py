import numpy as np
import pygame

speed = 0.1

# Funktion for lineær interpolation (lerp) mellem to punkter, så der laves en animation
def lerp(pos, targetPos, speed):
    return pos + (targetPos - pos) * speed

# Klasse for at repræsentere en boks
class Box:
    def __init__(self, pos, color, size, value) -> None:
        self.pos = pos
        self.size = size
        self.targetPos = pos
        self.color = color
        self.value = value

    def update(self):
        if np.linalg.norm(self.pos - self.targetPos) > 0.1:
            self.pos = lerp(self.pos, self.targetPos, speed)

    def show(self, screen):
        #box
        pygame.draw.rect(screen,self.color, pygame.Rect(self.pos[0], self.pos[1], self.size, self.size))

        #text
        #Dtermine font size based on box size
        #fontSize = int(self.size * 0.8)
        font = pygame.font.Font('freesansbold.ttf', int(self.size * 0.4) )
        text = font.render(str(self.value), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (self.pos[0] + self.size /2, self.pos[1] + self.size /2)
        screen.blit(text, textRect)

#Draw the boxes on the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#box = Box(np.array([0, 0]),(255,0,0), 1)
#box2 = Box(np.array([600, 0]),(0,0,255), 8)

arr = [1, 8]
#boxes = [box, box2]

def swapBoxes(boxIndex, boxIndex2, boxes):
    boxes[boxIndex].targetPos, boxes[boxIndex2].targetPos = boxes[boxIndex2].pos, boxes[boxIndex].pos

    #While the boxes are not in their target positions upodate the boxes and show all the boxes
    while np.linalg.norm(boxes[boxIndex].pos - boxes[boxIndex].targetPos) > 0.1 and np.linalg.norm(boxes[boxIndex2].pos - boxes[boxIndex2].targetPos) > 0.1:
        screen.fill((0, 0, 0))
        clock.tick(60)
        boxes[boxIndex].update()
        boxes[boxIndex2].update()
        showBoxes(boxes)
        pygame.display.update()

    boxes[boxIndex], boxes[boxIndex2] = boxes[boxIndex2], boxes[boxIndex]

def showBoxes(boxes):
    screen.fill((0, 0, 0))
    for box in boxes:
        box.show(screen)
    pygame.display.update()

def boxSort(algorithm, arr : list[float]) -> None:
    n = len(arr) 
    boxDistance = 800 / n 
    boxSize = boxDistance * 0.8

    for x, y, z in algorithm(arr):
        boxes = [Box(np.array([i * boxDistance, screen.get_height()/2 - boxSize/2]), (255, 255, 255), boxSize, arr[i]) for i in range(len(arr))]
        clock.tick(60)
        # Skal to bokse bytte plads?
        swap = x[y] != arr[y] or x[z] != arr[z]

        for i in range(len(boxes)):
            boxes[i].color = (0, 255, 0) if i == y else (255, 0, 0) if i == z else (255, 255, 255)
        showBoxes(boxes)

        if swap:
            swapBoxes(y, z, boxes)
            arr[y], arr[z] = arr[z], arr[y]



def bubble_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            yield temp, j + 1, j

def selection_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        min_index = i

        for j in range(i + 1, len(temp)):
            if temp[j] < temp[min_index]:
                min_index = j

        temp[i], temp[min_index] = temp[min_index], temp[i];
        yield temp, min_index, i

# insertion_sort(arr)
def insertion_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(1, len(temp)):
        key = temp[i]
        prev_indx = i - 1
        while prev_indx >= 0 and key < temp[prev_indx]:
            temp[prev_indx + 1] = temp[prev_indx]
            prev_indx -= 1
        temp[prev_indx + 1] = key
        yield temp, prev_indx + 1, i

def stalin_sort(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            arr.pop(i + 1)  # Remove the element at index i+1
        else:
            i += 1
        yield arr, i+1,i


boxSort(stalin_sort, [1, 5, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        

#while True:
#    for event in pygame.event.get(eventtype = pygame.KEYDOWN):
#        if pygame.key.name(event.key).lower() == 'c': break
#
#    screen.fill(0)
#    clock.tick(10)
#    box.show(screen)
#    box2.show(screen)
#
#    swapBoxes(0, 1, boxes)
#
#    pygame.display.update()