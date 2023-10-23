import numpy as np
import pygame

def lerp(pos, targetPos, speed):
    return pos + (targetPos - pos) * speed

class Box:
    def __init__(self, pos, color, value) -> None:
        self.pos = pos
        self.targetPos = pos
        self.speed = 0.1
        self.color = color
        self.value = value

    def update(self):
        if np.linalg.norm(self.pos - self.targetPos) > 0.1:
            self.pos = lerp(self.pos, self.targetPos, self.speed)

    def show(self, screen):
        pygame.draw.rect(screen,self.color, pygame.Rect(self.pos[0], self.pos[1], 50, 50))
        #font = pygame.font.Font(None, 36)
        #text = font.render(str(self.value), True, (0, 255, 0))
        #screen.blit(text, (self.pos[0] + 20, self.pos[1] + 20))


#Draw the boxes on the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#box = Box(np.array([0, 0]),(255,0,0))
#box2 = Box(np.array([300, 500]),(0,0,255))


#box2.targetPos, box.targetPos = box.pos, box2.pos

""" def await_keypress(key : str):
    while True:
        for event in pygame.event.get(eventtype = pygame.KEYDOWN):
            if pygame.key.name(event.key).lower() == key.lower(): return
        clock.tick(60)
        box.show(screen)
        box2.show(screen)
        pygame.display.update()
await_keypress('c') """


array = [1, 237,210,27,12,1,5]
#boxes = [Box(np.array([i * 100, 50]), (255, 255, 255)) for i in range(len(array))]


def swap(box1, box2, boxes, arr):
    box1.targetPos, box2.targetPos = box2.pos, box1.pos
    #box1.value, box2.value = box2.value, box1.value

    while True:
        clock.tick(120)
        box1.update()
        box2.update()
        

        screen.fill((0, 0, 0))
        for i in range(len(boxes)):
            boxes[i].show(screen)

        for i in range(len(arr)):
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(str(arr[i]), True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (boxes[i].pos[0] + 25, boxes[i].pos[1] + 25)
            screen.blit(text, textRect)

        pygame.display.update()
        
        if(np.linalg.norm(box1.pos - box1.targetPos) < 0.1 and np.linalg.norm(box2.pos - box2.targetPos) < 0.1):
            break

def bubble_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            yield temp, j + 1, j

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

def box_sort(algorithm, arr : list[float]) -> None:
    #boxes = [Box(np.array([i * 100, 50]), (255, 255, 255)) for i in range(len(arr))]
    boxes = [Box(np.array([i * 100, 50]), (255, 255, 255), arr[i]) for i in range(len(arr))]
    valueArray = arr.copy()
    #clock.tick(60)
    screen.fill((0, 0, 0))

    for x, y, z in algorithm(arr):
        boxes[y].color = (255, 0, 0)
        boxes[z].color = (0, 0, 255)
        swap(boxes[y], boxes[z], boxes, valueArray)
        valueArray[y], valueArray[z] = valueArray[z], valueArray[y]
        # Change the boxes array to reflect the new order
        boxes[y], boxes[z] = boxes[z], boxes[y]
        # Swap the box valeus
        boxes[y].color = (255, 255, 255)
        boxes[z].color = (255, 255, 255)
    print(valueArray)

#box_sort(bubble_sort, array)
print("New sort")
box_sort(bubble_sort, array)

""" while True and :
    clock.tick(120)
    screen.fill((0, 0, 0))

    for x, y, z in bubble_sort(array):
        boxes[y].color = (255, 0, 0)
        boxes[z].color = (0, 0, 255)
        print("swap", x[y], x[z])
        swap(boxes[y], boxes[z])
        # Change the boxes array to reflect the new order
        boxes[y], boxes[z] = boxes[z], boxes[y]
        boxes[y].color = (255, 255, 255)
        boxes[z].color = (255, 255, 255)
        

    print(x)

        

    pygame.display.update() """


#When I sort you must keep track of the indices, as the boxes represent array values, and there may be duplicates.
#The boxes must be sorted in the same way as the array is sorted.

