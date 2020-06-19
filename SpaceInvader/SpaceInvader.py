import pygame
import random, math
from  pygame import mixer

#initializing
pygame.init()
#create screen
screen = pygame.display.set_mode((800,600))


##background
background = pygame.image.load("background.png")
mixer.music.load("background.wav")
mixer.music.play()

#display title
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


##Player
playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerx_change= 0

##Enemy
enemyImage=[]
enemyX=[]
enemyY=[]
enemyx_change=[]
enemyy_change=[]
numberofEnemy =10
for i in range(numberofEnemy):
    enemyImage.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyx_change.append(4)
    enemyy_change.append(40)

##bullet
bullet = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bullet_ychange = 10
bullet_state = "Ready"

score =0
font = pygame.font.Font('CHICKEN Pie.ttf', 32)
textX =10
textY= 10
game_font = pygame.font.Font('Chasy.otf', 100)


def game_over():
    game_ov = font.render(" GAME OVER " , True, (0, 0, 0))
    screen.blit(game_ov, (255, 200))


def show_score (x,y):
    score_= font.render("SCORE: "+ str(score), True, (255,255,255))
    screen.blit(score_,(x,y))


def player (x,y):
    screen.blit(playerImage,(x,y))

def enemy (x,y,i):
    screen.blit(enemyImage[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state= "Fire"
    screen.blit(bullet, (x+18,y+20))


def collisonDetection (enemyX, enemyY, bulletX, bulletY):
    distance =math.sqrt((math.pow(enemyX-bulletX,2) )+ (math.pow(enemyY-bulletY,2)))
    if distance < 27 :
        return True
    else:
        return False

#Game Loop
running = True
while running:
    screen.fill((30,118,128))
    #background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerx_change = -3
            if event.key == pygame.K_RIGHT:
                playerx_change = 3
            if event.key ==pygame.K_SPACE:
                if bullet_state =="Ready":
                    bulletSound =  mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerx_change = 3

#player movement
    playerX += playerx_change
    if playerX <=0:
        playerX=0
    elif playerX >=736:
        playerX=736

    #Bullet Movement
    if bullet_state=="Fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bullet_ychange
    if bulletY <=0 :
        bulletY=480
        bullet_state="Ready"


##Enemy movement
    for  i in range(numberofEnemy):
        if enemyY[i] > 430:
            for j in range(numberofEnemy):
                enemyY[j]=2000
            game_over()
            break

        enemyX[i] += enemyx_change[i]
        if enemyX[i]<=0:
            enemyx_change[i] = 5
            enemyY[i] += enemyy_change[i]
        elif enemyX[i] >=736:
            enemyx_change[i]=-5
            enemyY[i] += enemyy_change[i]



##Collision
        collision =collisonDetection(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
                collisionsound = mixer.Sound("explosion.wav")
                collisionsound.play()
                bulletY= 480
                bullet_state="Ready"
                score +=1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()

