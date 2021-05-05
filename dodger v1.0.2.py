import pygame,sys,os,random,time
clock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

pygame.display.set_caption("Dodger")

win_size = (600,400)

screen = pygame.display.set_mode(win_size,0,32)

enemySpawnRatio = 20
enemyMinSize = 10
enemyMaxSize = 50
enemyMinSpeed = 2
enemyMaxSpeed = 5
playerMovSpeed = 6
FPS = 60
playerPos = pygame.Rect(300,200,50,50)
enemyScale = 10

enemyImage = pygame.image.load('baddie.png')
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()

def playerHitEnemy(playerRect,enemy):
    for b in enemy:
        if playerRect.colliderect(b['rect']):
            return True
    return False

while True:
    
    enemy = []
    score = 0
    playerRect.topleft = (300,330)
    moveLeft = moveRight = False
    enemys_counter = 0

    while True:
        score += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
                #print("KEY DOWN LEFT")
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
                #print("KEY DOWN RIGHT")

        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
                #print("KEY UP LEFT")
            if event.key == K_RIGHT:
                moveRight = False
                #print("KEY UP RIGHT")

        enemys_counter += 1

        if enemys_counter == enemySpawnRatio:
            #print("test")
            enemys_counter = 0
            enemySize = random.randint(enemyMinSize, enemyMaxSize)
            newEnemy = {'rect' : pygame.Rect(random.randint(0,600),0 - enemySize,enemySize,enemySize),
                        'speed' : random.randint(enemyMinSpeed,enemyMaxSpeed),
                        'surface' :pygame.transform.scale(enemyImage, (enemySize, enemySize)),
                        
                        }

            enemy.append(newEnemy)
            #print(enemy)

        if moveLeft and playerRect.left > 0:
             playerRect.move_ip(-1 * playerMovSpeed, 0)
        if moveRight and playerRect.right < 600:
             playerRect.move_ip(playerMovSpeed,0)

        for b in enemy:
            #print(b['rect']) 
            b['rect'].move_ip(0, b['speed'])

        for b in enemy[:]:
            if b['rect'].top > 600:
                enemy.remove(b)

        screen.fill((0,0,0))

        #print(score)

        screen.blit(playerImage,playerRect)
        #print()
        
        for b in enemy:
            screen.blit(b['surface'],b['rect'])

            
        pygame.display.update()

        if playerHitEnemy(playerRect,enemy):
            break

        mainClock.tick(FPS)

    
    print("you lost. Your score is:" , score)
    score = 0
    
    pygame.display.update()













    
