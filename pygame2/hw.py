import pygame
pygame.init()
screen=pygame.display.set_mode((500,400))
done=False
font = pygame.font.Font(None, 48)
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,60,60))
        pygame.display.flip()
        text_surface = font.render('Hello World', True, (255,255,255))
        screen.blit(text_surface, (150, 150))
        pygame.display.flip()

        