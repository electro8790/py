import pygame
pygame.init()
WINDOW_SIZE=(500,500)
screen=pygame.display.set_mode((WINDOW_SIZE))
pygame.display.set_caption("MY First Game screen")
screen.fill((58,58,58))
image = pygame.image.load("game_screen_image.png")
image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect()
image_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()