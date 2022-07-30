
import pygame
from object import Object
from random import randint

pygame.init()


pygame.display.set_caption("N-Back")



##### Settings #####

# fps
fps = 60
clock = pygame.time.Clock()
  
# color
color = {"black" : (0,0,0),"white":(255,255,255),"green":(0,255,0)}

# FPS
fps_clock = pygame.time.Clock()
fps = 60

# Count down timer
countdown = 4
last_count = pygame.time.get_ticks()




# Settings - Functions

# screen
def create_screen(width, height):
    global screen
    screen = pygame.display.set_mode((width, height))
    
    global screenwidth, screenheight
    screenwidth, screenheight = width, height


def update_screen(screen,color):
    screen.fill(color)  


# Program exit

def allow_to_exit_program():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run
            run = False
            pygame.quit()


########## Game Control ##########

# Ultimate control - to exit the game
run = True

# Main Menu

# Main Menu control - to exit the main menu
main = True

# How to play menu control - to exit the how to play menu
howtoplay = False

# Credit menu control - to exit the credit menu
credit = False

# Gameplay screen
game = False



# buttons
class Button:
    

    def __init__(self, font_name, size, x, y, color, text, center = False):
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
        if center == True:
            self.rect.center = x,y
        
        self.clicked = False
        self.hand = False

        self.move = 100


    def draw_text(self,screen):
        screen.blit(self.content, self.rect)


    def hovered(self,change_color,change_size, change_back_color = color["white"], change_back_size = 32,handshape = True, size_reset = False, x = 0,y = 0):
        active = False
        self.mouse_position = pygame.mouse.get_pos()
        
        # as we increase or dicrease the size of the text, the actual rect size doesn't change. 
        # so hovering over it is not applied accordingly. To prevent, I created this function.
        # if True, the changed text is still clickable - suitable for when increasing the size of the text.
        # if False, the changed text is not clickable - suitable for when decreasing the size of the text.
        if size_reset == True:
            self.rect = self.content.get_rect()
            self.rect.x = x
            self.rect.y = y
            
        
        if self.rect.collidepoint(self.mouse_position) and self.hand == False:
            self.hand = True
            print("hovered")
            if handshape:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.color = change_color
            self.size = change_size
            self.font_kind = pygame.font.Font(self.font_name,self.size)
            self.content = self.font_kind.render(self.text, True, self.color)
            active = True

        elif self.rect.collidepoint(self.mouse_position) == False and self.hand == True:
            self.hand = False
            print("hovered2")
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.color = change_back_color
            self.size = change_back_size
            self.font_kind = pygame.font.Font(self.font_name,self.size)
            self.content = self.font_kind.render(self.text, True, self.color)
          
        return active
        

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


    def key_movement(self):

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("up key pressed")
                    self.rect.y -= self.move
                if event.key == pygame.K_DOWN:
                    print("down key pressed")
                    self.rect.y += self.move
                if event.key == pygame.K_RETURN:
                    print("Enter key pressed")
                    return True
                if event.key == pygame.K_BACKSPACE:
                    print("Backspace key pressed")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.move = 0
                if event.key == pygame.K_DOWN:
                    self.move = 0
        
            self.move = 100


##### From here is instantiations and calling functions #####

# Create screen
create_screen(800,800)


# Main Menu buttons
main_mainmenu_button = Button("8bitwonder.ttf",64,screenwidth/2,100,color['white'],"Main Menu",True)
main_start_button = Button("8bitwonder.ttf",32,screenwidth/2, 220,color['white'],"Start",True)
main_howtoplay_button = Button("8bitwonder.ttf",32,screenwidth/2,320,color['white'],"How to play",True)
main_credit_button = Button("8bitwonder.ttf",32,screenwidth/2,420,color['white'],"Credit",True)
main_exit_button = Button("8bitwonder.ttf",32,screenwidth/2,520,color['white'],"Exit",True)
main_x_button = Button("8bitwonder.ttf",24,screenwidth/2-200,0,color['white'],"*",False)


# How to play buttons
howtoplay_title_button = Button("8bitwonder.ttf",32,250,220,color['white'],"How to play")
howtoplay_back_button = Button("8bitwonder.ttf",42,250,520,color['white'],"Back")

howtoplay_title_button.rect.center = screenwidth/2, screenheight/2 - 300
howtoplay_back_button.rect.center = screenwidth/2, screenheight/2 + 200

# Credit Menu buttons
credit_title_button = Button("8bitwonder.ttf", 42,250,220,color['white'], "Credit")
credit_made_by_button = Button("8bitwonder.ttf",64,250,320,color['white'],"Jinsung Kim")
credit_back_button_button = Button("8bitwonder.ttf",42,250,520,color['white'],"Back")

credit_title_button.rect.center = screenwidth/2, screenheight/2 - 200
credit_made_by_button.rect.center = screenwidth/2, screenheight/2 - 100
credit_back_button_button.rect.center = screenwidth/2, screenheight/2 + 200

# Create player
player1 = Object(0,screenheight/2,10,100,1,True,False)
player2 = Object(screenwidth,screenheight/2,10,100,1,True,False)
ball = Object(screenwidth/2,screenheight/2,50,50,2,True,False)

# countdown
countdown_button = Button("gameplay.ttf",18,screenwidth/2,400,color["white"],str(countdown),False)

# how to play objects
n1 = Button("gameplay.ttf",36,screenwidth/8,300,color["white"],"1")
n2 = Button("gameplay.ttf",36,screenwidth/8*2,300,color["white"],"2")
n3 = Button("gameplay.ttf",36,screenwidth/8*3,300,color["green"],"1")
n4 = Button("gameplay.ttf",36,screenwidth/8*4,300,color["white"],"1")
n5 = Button("gameplay.ttf",36,screenwidth/8*5,300,color["white"],"3")
n6 = Button("gameplay.ttf",36,screenwidth/8*6,300,color["white"],"5")
n7 = Button("gameplay.ttf",36,screenwidth/8*7,300,color["green"],"3")

n1.show = False
n2.show = False
n3.show = False
n4.show = False
n5.show = False
n6.show = False
n7.show = False

two_back = Button("8bitwonder.ttf",42,screenwidth/2,210,color["green"],"2 Back",True)
answer_text = Button("8bitwonder.ttf",28,50,455,color["white"],"answer")
n3_answer = Button("gameplay.ttf",36,screenwidth/8*3,450,color["green"],"O")
n4_answer = Button("gameplay.ttf",36,screenwidth/8*4,450,color["white"],"X")
n5_answer = Button("gameplay.ttf",36,screenwidth/8*5,450,color["white"],"X")
n6_answer = Button("gameplay.ttf",36,screenwidth/8*6,450,color["white"],"X")
n7_answer = Button("gameplay.ttf",36,screenwidth/8*7,450,color["green"],"O")

matching_number_arrow1 = Object(screenwidth/8*2,400,15,15,1,False,True,"arrows.png")
matching_number_arrow2 = Object(screenwidth/8*5,400,15,15,1,False,True,"arrows.png")

while run:
    
    update_screen(screen, color["black"])
    # print(pygame.mouse.get_pos())
    # print(main_x_button.rect)
    # Main Menu screen
    if main == True:
        ball.location_reset(screenwidth,screenheight)
        if howtoplay == True:
            #print(pygame.mouse.get_pos())
            count_timer = pygame.time.get_ticks()
            
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer
                print(f"countdown : {countdown}")
                countdown_button.content = countdown_button.font_kind.render(str(countdown),True, countdown_button.color)
            
            two_back.draw_text(screen)
            n1.show,n2.show,n3.show = True,True,True
            matching_number_arrow1.draw_on_screen(screen,150,370)

            n3_answer.draw_text(screen)
            answer_text.draw_text(screen)
            if countdown <= -0:
                n4.show = True
            if countdown <= -3:
                n5.show = True
            if countdown <= -6:
                n6.show = True
            if countdown <= -9:
                n7.show = True
            if countdown <= -19:
                n1.show,n2.show,n3.show,n4.show,n5.show,n6.show,n7.show = False,False,False,False,False,False,False
                countdown = 2

            if n1.show == True:
                n1.draw_text(screen)
            if n2.show == True:
                n2.draw_text(screen)
            if n3.show == True:
                n3.draw_text(screen)
            if n4.show == True:
                n4.draw_text(screen)
                n4_answer.draw_text(screen)
            if n5.show == True:
                n5.draw_text(screen)
                n5_answer.draw_text(screen)
            if n6.show == True:
                n6.draw_text(screen)
                n6_answer.draw_text(screen)
            if n7.show == True:
                n7.draw_text(screen)
                n7_answer.draw_text(screen)
                matching_number_arrow2.draw_on_screen(screen,556,370)


           
            howtoplay_title_button.draw_text(screen)
            howtoplay_back_button.draw_text(screen)

            howtoplay_title_button.hovered(color['green'], 32, color['white'], 32,handshape = False)
            
            howtoplay_back_button.hovered(color['green'],42,color['white'],42, False)

            if howtoplay_back_button.check_click():
                
                # game control - howtoplay menu exit
                howtoplay = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        print("backspace key pressed")
                        main_x_button.content = main_x_button.font_kind.render(main_x_button.text,True, color['white'])
                        howtoplay = False

        elif credit == True:

            credit_title_button.draw_text(screen)
            credit_made_by_button.draw_text(screen)
            credit_back_button_button.draw_text(screen)
            
            credit_title_button.hovered(color['green'],42,color['white'],42,False,x=credit_title_button.rect.x, y = credit_title_button.rect.y)
            credit_made_by_button.hovered(color['green'],64,color['white'],64,False,x=credit_made_by_button.rect.x, y = credit_made_by_button.rect.y)
            

            credit_back_button_button.hovered(color['green'],42,color['white'],42,False,x=credit_back_button_button.rect.x, y = credit_back_button_button.rect.y)


            if credit_back_button_button.check_click():
                print("back button clicked")

                # game control - credit menu exit
                credit = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        print("backspace key pressed")
                        main_x_button.content = main_x_button.font_kind.render(main_x_button.text,True, color['white'])
                        credit = False
            
        else:

            main_mainmenu_button.draw_text(screen)
            main_start_button.draw_text(screen)
            main_howtoplay_button.draw_text(screen)
            main_credit_button.draw_text(screen)
            main_exit_button.draw_text(screen)
            main_x_button.draw_text(screen)

            main_start_button.hovered(color['green'],42, color['white'],32,True,True,main_start_button.rect.x,main_start_button.rect.y)
            main_howtoplay_button.hovered(color['green'],36,color['white'],32,False, 250,320)
            main_credit_button.hovered(color['green'],32,color['white'],32,False)
            main_exit_button.hovered((130,130,130),25,color['white'],32,False)

            if main_start_button.check_click():
                print("start menu clicked")
                game = True
                main = False
            if main_credit_button.check_click():
                print("credit menu clicked")
                credit = True
            if main_howtoplay_button.check_click():
                print("how to play menu clicked")
                howtoplay = True
            if main_exit_button.check_click():
                run = False
            

            if main_x_button.key_movement():
                
                if main_x_button.rect.y < 250:
                    print("START!!!")
                    game = True
                    main = False
                elif main_x_button.rect.y < 350:
                    print("HOW TO PLAY pressed")
                    main_howtoplay_button.color = color['green']
                    howtoplay = True
                elif main_x_button.rect.y < 450:
                    print("CREDIT pressed")
                    credit = True
                elif main_x_button.rect.y < 550:
                    print("EXIT pressed")
                    run = False

            if main_x_button.rect.y < 205:
                main_x_button.rect.y = 205
            if main_x_button.rect.y > 505:
                main_x_button.rect.y = 505
    
    # Game screen
    elif game == True:
        main = False
        update_screen(screen,color["green"])
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        


        player1.draw_on_screen(screen,0,screenheight/2,(0,0,0))
        player2.draw_on_screen(screen,screenwidth,screenheight/2,(0,0,0))

        player1.key_movement(10,False)
        player2.key_movement(10,True)

        player1.limit_movement(0,50,0,screenheight)
        player2.limit_movement(screenwidth-50,screenwidth,0,screenheight)

        ball.draw_on_screen(screen,screenwidth/2,screenheight/2,(0,0,0))
        ball.automactic_movement(screenwidth,screenheight)

        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            print("collided")
            ball.x_speed *= -1
        if ball.rect.left <= 0:
            print("player2 Won!")
            main = True
            game = False
        elif ball.rect.right >= screenwidth:
            print("player1 Won")
            main = True
            game = False
        
        

        
        

     
        #ball.limit_movement(screenwidth,screenheight)
        
        
        
        




    allow_to_exit_program()

    pygame.display.flip()
    fps_clock.tick(fps)
    
