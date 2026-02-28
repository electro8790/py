import math
import random
import pygame


SCREENWIDTH = 900
SCREENHEIGHT = 700
PLAYERSTARTX = 370
PLAYERSTARTY = 380
ENEMYSTARTYMIN = 50
ENEMYSTARTYMAX = 170
ENEMYSPEEDX = 4
ENEMYSPEEDY = 40
BULLETSPEEDY = 10
COLLISIONDISTANCE = 30
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerimg=pygame.image.load("player.png")
playerX=PLAYERSTARTX
playerY=PLAYERSTARTY
playerX_change=0
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
numofenemies=6
for i in range(numofenemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREENWIDTH-64))
    enemyY.append(random.randint(ENEMYSTARTYMIN,ENEMYSTARTYMAX))
    enemyX_change.append(ENEMYSPEEDX)
    enemyY_change.append(ENEMYSPEEDY)
bulletimg=pygame.image.load("bullet.png")
bulletX=0
bullety=playerY
bulletX_change=0
bulletY_change=BULLETSPEEDY
bullet_state="ready"
