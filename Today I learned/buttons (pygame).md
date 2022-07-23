# 7/23 Today I learned...

# Buttons in pygame

- Create Button class and use its instances in the game
- screen.blit() methods in Button class should be called inside of game loop
- Hovering over effect - pygame.mouse.get_pos()
- Mouse Click event - set a variable 'self.clicked = False'
- Set another variable in constructor if Button class is used in another module

```py
import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))
screenwidth = screen.get_width()
screenheight = screen.get_height()

start_img = pygame.image.load("start.png")

exit_img = pygame.image.load("exit.png")

class Button:

    def __init__(self,x,y,image,scale,name):
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.name = name
    
    def draw(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))  # 'self.rect.x' returns x position for (top) left corner

    def mouse_working(self):
        self.pos = pygame.mouse.get_pos()   # 'get_pos()' returns tuple like (0,0)
        #print(self.pos) # check mouse position
        if self.rect.collidepoint(self.pos): # mouse hover
            pygame.time.delay(30) # delay 30 milleseconds after hovering over button
            self.rect.topleft = (self.x - 10, self.y -10) # hovering over effect
            if pygame.mouse.get_pressed()[0] and self.clicked == False: #'get_pressed()' returns tuple (False,False,False)
                print(f"{self.name} clicked")
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == False and self.clicked == True:
                self.clicked = False
        else:
            self.rect.topleft = (self.x,self.y)



start_button = Button(screenwidth/6 ,screenheight/2 - 2*start_img.get_height(), start_img, 3, "start")
exit_botton = Button(screenwidth/5*3, screenheight/2 - 2*exit_img.get_height(), exit_img, 3, "exit")

run= True
while run:
    
    screen.fill((202,228,241))

    start_button.draw()

    exit_botton.draw()

    start_button.mouse_working()

    exit_botton.mouse_working()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
```
