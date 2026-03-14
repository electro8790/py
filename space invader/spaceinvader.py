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
background = pygame.image.load("background.png")
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
scorevalue=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
overfont=pygame.font.Font('freesansbold.ttf',64)
def showscore(x,y):
    score=font.render('Score:'+str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))
def gameovertext():
    overtext=overfont.render('GAME OVER',True,(255,255,255))
    screen.blit(overtext,(200,300))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def firebullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2))
    return distance< COLLISIONDISTANCE
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletX=playerX
                    firebullet(bulletX,bullety)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
    playerX+=playerX_change
    playerX=max(0,min(playerX,SCREENWIDTH-64))
    for i in range(numofenemies):
        if enemyY[i]>340:
            for j in range(numofenemies):
                enemyY[j]=2000
                gameovertext()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0 or enemyX[i]>=SCREENWIDTH-64:
            enemyX_change[i]*=-1
            enemyY[i]+=enemyY_change[i]
    if iscollision(enemyX[i],enemyY[i],bulletX,bullety):
        bullety=PLAYERSTARTY
        bullet_state="ready"
        scorevalue+=1
        enemyX[i]=random.randint(0,SCREENWIDTH-64)
        enemyY[i]=random.randint(ENEMYSTARTYMIN,ENEMYSTARTYMAX)
        enemy(enemyX[i],enemyY[i],i)
    if bullety <= 0:
        bullety = PLAYERSTARTY
        bullet_state = "ready"
    elif bullet_state == "fire":
        firebullet(bulletX, bullety)
        bullety -= bulletY_change
    player(playerX,playerY)
    showscore(textX,textY)
    pygame.display.update()

