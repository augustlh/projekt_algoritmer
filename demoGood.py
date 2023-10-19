import numpy as np
import pygame

speed = 0.1

# Funktion for lineær interpolation (lerp) mellem to punkter, så der laves en animation
def lerp(pos, targetPos, speed):
    return pos + (targetPos - pos) * speed

# Klasse for at repræsentere en boks
class Box:
    def __init__(self, pos, color) -> None:
        self.pos = pos
        self.targetPos = pos
        self.color = color

    def update(self):
        if np.linalg.norm(self.pos - self.targetPos) > 0.1:
            self.pos = lerp(self.pos, self.targetPos, speed)

    def show(self, screen):
        pygame.draw.rect(screen,self.color, pygame.Rect(self.pos[0], self.pos[1], 50, 50))

#Draw the boxes on the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
box = Box(np.array([0, 0]),(255,0,0))
box2 = Box(np.array([0, 100]),(0,0,255))

arr = [1, 8]
boxes = [box, box2]

def swapBoxes(box1, box2):
    pass

while True:
    for event in pygame.event.get(eventtype = pygame.KEYDOWN):
        if pygame.key.name(event.key).lower() == 'c': break
    clock.tick(60)
    box.show(screen)
    box2.show(screen)

    #Draw the array values on the screen over the corresponding boxes. the boxes array is used to get which number is in which box
    for i in range(len(arr)):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(arr[i]), True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (boxes[i].pos[0] + 25, boxes[i].pos[1] + 25)
        screen.blit(text, textRect)

        


    pygame.display.update()