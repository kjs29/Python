# 7/27 Today I learned...

# How to create movable objects(rectangles) in pygame

1. To create movable objects in pygame library, we need to create surfaces
2. surfaces can't move, so we make rectangles around the surfaces!
3. There are at least two ways I have learned to create rectangles.

<em>first way</em>
```py
import pygame

pygame.init()

# create main surface(screen)
screen = pygame.display.set_mode((1200,800))

# create regular surface(object)
rect1 = pygame.Rect(400,500,15,15)

heldkeys = set()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                heldkeys.add("down")
            if event.key == pygame.K_UP:
                heldkeys.add("up")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                heldkeys.remove("down")
            if event.key == pygame.K_UP:
                heldkeys.remove("up")
    for _ in heldkeys:
        if "up" in heldkeys:
            rect1.y -= 1
        if "down" in heldkeys:
            rect1.y += 1
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), rect1)
    pygame.display.flip()
```

<em>second way</em>
```py
import pygame

pygame.init()

# create main surface(screen)
screen = pygame.display.set_mode((1200,800))

# create regular surface(object)
surface1 = pygame.Surface((15,15))
surface1.fill((0,255,0))
surface1_rect = surface1.get_rect()
surface1_rect.topleft = 400,500
heldkeys = set()
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                heldkeys.add("down")
            if event.key == pygame.K_UP:
                heldkeys.add("up")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                heldkeys.remove("down")
            if event.key == pygame.K_UP:
                heldkeys.remove("up")
    for _ in heldkeys:
        if "up" in heldkeys:
            surface1_rect.y -= 1
        if "down" in heldkeys:
            surface1_rect.y += 1
    screen.fill((0,0,0))
    screen.blit(surface1,surface1_rect)
    pygame.display.flip()
```

They both create a rectangle with (15,15) size at (400,500), with color green(0,255,0)
