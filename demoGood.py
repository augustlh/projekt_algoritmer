import numpy as np
import pygame

# Funktion for lineær interpolation (lerp) mellem to punkter, så der laves en animation
def lerp(pos, targetPos, speed):
    return pos + (targetPos - pos) * speed

# Klasse for at repræsentere en boks
class Box:
    def __init__(self, pos, color) -> None:
        self.pos = pos
        self.targetPos = pos
        self.speed = 0.1
        self.color = color

    def update(self):
        if np.linalg.norm(self.pos - self.targetPos) > 0.1:
            self.pos = lerp(self.pos, self.targetPos, self.speed)

    def show(self, screen):
        pygame.draw.rect(screen,self.color, pygame.Rect(self.pos[0], self.pos[1], 50, 50))

#Draw the boxes on the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
box = Box(np.array([0, 0]),(255,0,0), 0)
box2 = Box(np.array([300, 500]),(0,0,255), 2)

while True:
    for event in pygame.event.get(eventtype = pygame.KEYDOWN):
        if pygame.key.name(event.key).lower() == 'c': break
    clock.tick(60)
    box.show(screen)
    box2.show(screen)
    pygame.display.update()