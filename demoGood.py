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
        clock.tick(30)
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

    boxes = [Box(np.array([i * boxDistance, screen.get_height()/2 - boxSize/2]), (255, 255, 255), boxSize, arr[i]) for i in range(len(arr))]

    print("ArrayØ:", arr)
    for x, y, z in algorithm(arr):
        clock.tick(10)
        print("Array:", x, y, z)
        
        #If all the values in x are not the same as the values in arr then set var swap to true
        swap = False

        for i in range(len(x)):
            if x[i] != arr[i]:
                swap = True
                break
        
        for box in boxes:
            box.color = (255, 255, 255)

        #Change the color of the boxes that are being compared
        boxes[y].color = (255, 0, 0)
        boxes[z].color = (0, 0, 255)

        showBoxes(boxes)

        #If swap is true then swap the boxes
        if swap:
            swapBoxes(y, z, boxes)
            arr[y], arr[z] = arr[z], arr[y]

        print("Boxes:", [box.value for box in boxes])

        #y and z er index for de to boxes der sammenlignes
        #
        


def bubble_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            yield temp, j + 1, j


boxSort(bubble_sort, [1, 5, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        

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