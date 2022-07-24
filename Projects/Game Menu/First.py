import pygame

pygame.init()

screenwidth = 800
screenheight = 800
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Practice clicking buttons")
white = (255,255,255)
black = (0, 0, 0)

# Game Control 

# Ultimate control - to exit the game
run = True

# Main Menu control - to exit the main menu
main = False

# Credit menu control - to exit the credit menu
credit = False


class Button:
    
    def __init__(self, font_name, size, x, y, color, text):
        self.font_name = font_name
        self.color = color
        self.text = text
        self.size = size

        self.font_kind = pygame.font.Font(self.font_name,size)
        self.content = self.font_kind.render(self.text,True, self.color)
        self.rect = self.content.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        #if I want to make it centered automatically
        #self.rect.center = x,y
        self.clicked = False
        self.hand = False


    def draw_text(self,screen):
        screen.blit(self.content, self.rect)

    def hovered(self):

        self.mouse_position = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.mouse_position) and self.hand == False:
            self.hand = True
            print("hovered")
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.color = (0,255,0)
            self.content = self.font_kind.render(self.text, True, self.color)

            return True

        elif self.rect.collidepoint(self.mouse_position) == False and self.hand == True:
            self.hand = False
            print("hovered2")
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.color = white
            self.content = self.font_kind.render(self.text, True, self.color)
            
            return False
        
    def check_click(self):
        self.mouse_position = pygame.mouse.get_pos()
        active = False
        if self.rect.collidepoint(self.mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                active = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False

        return active



# Main Menu buttons
startmenu = Button("8bitwonder.ttf",32,250, 220,white,"Start")
howtoplaymenu = Button("8bitwonder.ttf",32,250,320,white,"How to play")
creditmenu = Button("8bitwonder.ttf",32,250,420,white,"Credit")
exitmenu = Button("8bitwonder.ttf",32,250,520,white,"Exit")

# Credit Menu buttons
credit_title = Button("8bitwonder.ttf", 42,250,220,white, "Credit")
credit_made_by_whom = Button("8bitwonder.ttf",64,250,320,white,"Jinsung Kim")
credit_back_button = Button("8bitwonder.ttf",42,250,520,white,"Back")

credit_title.rect.center = screenwidth/2, screenheight/2 - 200
credit_made_by_whom.rect.center = screenwidth/2, screenheight/2 - 100
credit_back_button.rect.center = screenwidth/2, screenheight/2 + 200

while run:
    
    screen.fill(black)
    
    
    
    if credit == True:
        
        credit_title.draw_text(screen)
        credit_made_by_whom.draw_text(screen)
        credit_back_button.draw_text(screen)
        
        credit_title.hovered()
        credit_made_by_whom.hovered()
        credit_back_button.hovered()


        if credit_back_button.check_click():
            print("back button clicked")

            credit = False
            
    else:
        startmenu.draw_text(screen)
        howtoplaymenu.draw_text(screen)
        creditmenu.draw_text(screen)
        exitmenu.draw_text(screen)
        
        if startmenu.hovered():
            startmenu.size = 42
            startmenu.font_kind = pygame.font.Font(startmenu.font_name,startmenu.size)
            startmenu.content = startmenu.font_kind.render(startmenu.text,True, startmenu.color)
            startmenu.rect = startmenu.content.get_rect()
            startmenu.rect.x = 250
            startmenu.rect.y = 220
        else:
            startmenu.size = 32
            startmenu.font_kind = pygame.font.Font(startmenu.font_name,startmenu.size)
        howtoplaymenu.hovered()
        if creditmenu.hovered():
            creditmenu.color = (0,50,105)
            creditmenu.content = creditmenu.font_kind.render(creditmenu.text, True, creditmenu.color)
        if exitmenu.hovered():
            exitmenu.color = (130,130,130)
            exitmenu.size = 22
            exitmenu.font_kind = pygame.font.Font(exitmenu.font_name,exitmenu.size)
            exitmenu.content = exitmenu.font_kind.render(exitmenu.text,True, exitmenu.color)
        else:
            exitmenu.size = 32
            exitmenu.font_kind = pygame.font.Font(exitmenu.font_name,exitmenu.size)



        if startmenu.check_click():
            print("start menu clicked")
        if creditmenu.check_click():
            print("credit menu clicked")
            credit = True
        if howtoplaymenu.check_click():
            print("how to play menu clicked")
        if exitmenu.check_click():
            run = False
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
 
    pygame.display.flip()
