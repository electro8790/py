import pygame
screen_width,Screenheight=400,500
pygame.init()
screen =pygame.display.set_mode((screen_width,Screenheight))
pygame.display.set_caption('Adding background image and image')
background_image=pygame.transform.scale(pygame.image.load('pygame1\OIP.jpg').convert(),(screen_width,Screenheight))
penguin=pygame.transform.scale(pygame.image.load('pygame1\OIF.jpg').convert_alpha(),(200,200))
penguin_rect=penguin.get_rect(center=(screen_width//2,Screenheight//2))
text=pygame.font.Font(None,38).render('hello world',True,pygame.Color('white'))
text_rect=text.get_rect(center=(screen_width//2,Screenheight//2+110))
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin,penguin_rect)
        display_surface.blit(text,text_rect)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=='__main__':
    game_loop()                                                      
