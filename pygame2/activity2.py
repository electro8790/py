import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,255,255))
Green=(0,255,0)
pygame.draw.circle(screen,Green,(300,300),50)
pygame.draw.circle(screen,Green,(100,100),78,3)
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()