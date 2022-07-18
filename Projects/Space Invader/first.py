"""
to download pygame module:
pip install pygame

download png(image of enemy, player) : www.flaticon.com
download background image : www.freepik.com
download font : www.dafont.com
"""

import pygame
import random
import math
from pygame import mixer


#initialize the pygame
pygame.init()

# creae the screen that has the size of (width,height)
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")

# background sound
mixer.music.load("background.mp3")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("eel.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("octopus.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy (multiple)
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("crab.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("starfish.png")
bulletX = 2000
bulletY = 2000
bulletY_change = 8
bullet_state = "ready"

# Font
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10

# life
lives = 3
life = pygame.font.Font("freesansbold.ttf", 32)

# game over
gameover = False

# game over text
over_font = pygame.font.Font("freesansbold.ttf",64)

# random triggering variable for game over 
trigger = False

# show lives
def show_lives():
    life_display = life.render(f"life : {lives}",True, (255,255,255))
    screen.blit(life_display, (690, 10))

def show_score(x,y):
    score = font.render("Score : "+ str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over,(200,250))

def player(x,y):
    screen.blit(playerImg,(x, y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x, y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY ,2))
    if distance < 27:
        return True
    else:
        return False

def stop_sound():
    pygame.mixer.pause()

# Game loop
running = True

while running:
    
    #RGB - red, green, blue
    screen.fill((0,0,0))
    
    # Background image
    screen.blit(background,(0,0))
    
 
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:

                playerX_change = -5
                
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                
            if event.key == pygame.K_UP:
                playerY_change = -5
                
            if event.key == pygame.K_DOWN:
                playerY_change = 5
            
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # get the current x,y coordinate of the spaceship
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = playerY_change = 0
    
    # decide how much player moves left or right 
    playerX += playerX_change
    playerY += playerY_change

    # checking for boundaries of player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536
    
    # show how much each enemy moves
    for i in range(num_of_enemies):
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        if enemyY[i] >= 550:
            lives -= 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
    
        # Collision between enemy and bullet
        collision_enemy_bullet = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision_enemy_bullet:
            bulletY = 20000
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
            explosion_sound_enemy = mixer.Sound("boing_poing.wav")
            explosion_sound_enemy.play()

        # show much enemy moves
        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i], enemyY[i], i)

        collision_enemy_player = isCollision(enemyX[i], enemyY[i], playerX, playerY)
        if collision_enemy_player:
            explosion_sound_player = mixer.Sound("explosion.wav")
            explosion_sound_player.play()
            for each in range(num_of_enemies):
                enemyX[each] = random.randint(0,735)
                enemyY[each] = random.randint(50,150)
            playerX = 370
            playerY = 480
            lives -= 1
 
        # gameover
        if lives == 0:
            gameover =  True
        if gameover:
            for j in range(num_of_enemies):
                enemyX_change[j] = 0
                enemyY[j] = -2000
            trigger = True
        if trigger:
            game_over_text()
            show_score(299,330)
            break
           
    # bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire": 
        
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY)
    show_score(textX, textY)
    show_lives()

    #update the entire display if there is no parameter
    # pygame.display.update() is equivalent to pygame.display.flip()
    pygame.display.update()

