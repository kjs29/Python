
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
color = {"black" : (0,0,0),"white":(255,255,255),"green":(0,255,0),"grey":(175,173,169)}

# FPS
fps_clock = pygame.time.Clock()
fps = 60

# Count down timer
countdown = 4
last_count = pygame.time.get_ticks()
last_count2 = pygame.time.get_ticks()



# Settings - Functions

# screen
def create_screen(width, height):
    global screen
    screen = pygame.display.set_mode((width, height))
    
    global screenwidth, screenheight
    screenwidth, screenheight = width, height


def update_screen(screen, color):
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
    

    def __init__(self, font_name, size, x, y, color, text, center = False, image = False, imagefile_name = None):
        
        
        self.image = image
        if image == False:
            self.font_name = font_name
            self.color = color
            self.text = text
            self.size = size

            self.font_kind = pygame.font.Font(self.font_name, size)
            self.content = self.font_kind.render(self.text,True, self.color)
            self.rect = self.content.get_rect()
        else:
            self.image = pygame.image.load(imagefile_name)
            self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #if I want to make it centered automatically
        if center == True:
            self.rect.center = x, y
        
        self.clicked = False
        self.hand = False

        self.move = 100


    def draw_text(self, screen):
        if self.image == False:
            screen.blit(self.content, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.image,(self.rect.x, self.rect.y))

    def hovered(self,change_color, change_size, change_back_color = color["white"], change_back_size = 32,handshape = True, size_reset = False, x = 0, y = 0):
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
            if self.image == False:
                self.color = change_color
                self.size = change_size
                self.font_kind = pygame.font.Font(self.font_name, self.size)
                self.content = self.font_kind.render(self.text, True, self.color)
            active = True

        elif self.rect.collidepoint(self.mouse_position) == False and self.hand == True:
            self.hand = False
            print("hovered2")
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if self.image == False:
                self.color = change_back_color
                self.size = change_back_size
                self.font_kind = pygame.font.Font(self.font_name, self.size)
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

    def disappear(self):
        self.rect.center = -2000,-2000
    
    def update(self,x,y):
        self.rect.x = x
        self.rect.y = y


##### From here is instantiations and calling functions #####

# Create screen
create_screen(800,800)


# Main Menu buttons
main_mainmenu_button = Button("8bitwonder.ttf", 64, screenwidth / 2, 100, color['white'], "Main Menu", True)
main_start_button = Button("8bitwonder.ttf", 32, screenwidth / 2, 220, color['white'], "Start", True)
main_howtoplay_button = Button("8bitwonder.ttf", 32, screenwidth / 2, 320, color['white'], "How to play", True)
main_credit_button = Button("8bitwonder.ttf", 32, screenwidth / 2, 420, color['white'], "Credit", True)
main_exit_button = Button("8bitwonder.ttf", 32, screenwidth / 2, 520, color['white'], "Exit", True)
main_x_button = Button("8bitwonder.ttf", 24, screenwidth / 2 - 200, 0, color['white'], "*", False)


# How to play buttons
howtoplay_title_button = Button("8bitwonder.ttf", 32, 250, 220, color['white'], "How to play")
howtoplay_back_button = Button("8bitwonder.ttf", 42, 250, 520, color['white'], "Back")

howtoplay_title_button.rect.center = screenwidth / 2, screenheight / 2 - 300
howtoplay_back_button.rect.center = screenwidth / 2, screenheight / 2 + 300

# Credit Menu buttons
credit_title_button = Button("8bitwonder.ttf", 42, 250, 220, color['white'], "Credit")
credit_made_by_button = Button("8bitwonder.ttf", 64, 250, 320, color['white'], "Jinsung Kim")
credit_back_button_button = Button("8bitwonder.ttf", 42, 250, 520, color['white'], "Back")

credit_title_button.rect.center = screenwidth / 2, screenheight / 2 - 200
credit_made_by_button.rect.center = screenwidth / 2, screenheight / 2 - 100
credit_back_button_button.rect.center = screenwidth / 2, screenheight / 2 + 200

# countdown - how to paly menu
countdown_button = Button("gameplay.ttf", 18, screenwidth / 2, 400, color["white"], str(countdown), False)

# buttons & objects in How to play menu
n1 = Button("gameplay.ttf", 36, screenwidth / 8, 300, color["white"], "1")
n2 = Button("gameplay.ttf", 36, screenwidth / 8 * 2, 300, color["white"], "2")
n3 = Button("gameplay.ttf", 36, screenwidth / 8 * 3, 300, color["white"], "1")
n4 = Button("gameplay.ttf", 36, screenwidth / 8 * 4, 300, color["white"], "1")
n5 = Button("gameplay.ttf", 36, screenwidth / 8 * 5, 300, color["white"], "3")
n6 = Button("gameplay.ttf", 36, screenwidth / 8 * 6, 300, color["white"], "5")
n7 = Button("gameplay.ttf", 36, screenwidth / 8 * 7, 300, color["white"], "3")

n1_clone = Button("gameplay.ttf", 36, screenwidth / 8, 300, color["white"], "1")
n2_clone = Button("gameplay.ttf", 36, screenwidth / 8 * 2, 300, color["white"], "2")
n3_clone = Button("gameplay.ttf", 36, screenwidth / 8 * 3 , 300, color["white"], "1")
n4_clone = Button("gameplay.ttf", 36, screenwidth / 8 * 4, 300, color["white"], "1")
n5_clone = Button("gameplay.ttf", 36, screenwidth / 8 * 5, 300, color["white"], "3")

count_2back = Button("gameplay.ttf", 16, 120, 370, color["green"], "2-back")
count_1back = Button("gameplay.ttf", 16, 230, 370, color["green"], "1-back")

count_2back.rect.x = -200
count_2back.rect.y = -200
count_1back.rect.x = -200
count_1back.rect.y = -200

two_back = Button("8bitwonder.ttf", 42, screenwidth / 2, 210, color["green"], "2 Back", True)
answer_text = Button("8bitwonder.ttf", 28, 50, 500, color["white"], "answer")
n3_answer = Button("gameplay.ttf", 36, screenwidth / 8 * 3, 500, color["green"], "O")
n4_answer = Button("gameplay.ttf", 36, screenwidth / 8 * 4, 500, color["white"], "X")
n5_answer = Button("gameplay.ttf", 36, screenwidth / 8 * 5, 500, color["white"], "X")
n6_answer = Button("gameplay.ttf", 36, screenwidth / 8 * 6, 500, color["white"], "X")
n7_answer = Button("gameplay.ttf", 36, screenwidth / 8 * 7, 500, color["green"], "O")

matching_number_arrow1 = Object(-200, -200, 15, 15, 1, False, True, "left_arrow.png")
matching_number_arrow2 = Object(-200, -200, 15, 15, 1, False, True, "left_arrow.png")

matching_number_arrow2.rect.x = -200
matching_number_arrow2.rect.y = -200
matching_number_arrow1.rect.x = -200
matching_number_arrow1.rect.y = -200


# Buttons & objects in Game screen

# start, finish, car images
start_image = pygame.image.load("start.png")
finish_image = pygame.image.load("goal.png")
car_image = pygame.image.load("sportcar.png")

car_image_rect = car_image.get_rect()
car_image_rect.x = 110
car_image_rect.y = 110


# countdown related 
lst = []
lst_rendered_contents = []
lst_rect = []
number_of_questions = 5
for i in range(number_of_questions):
    lst.append(randint(1, 9))
print(lst)
for each in lst:
    each_number = pygame.font.Font("gameplay.ttf", 164)
    each_content = each_number.render(str(each), True, color["white"])
    each_rect = each_content.get_rect()
    lst_rendered_contents.append(each_content)
    lst_rect.append(each_rect)

# countdown before start
countdown_before_start = -4
countdown_before_start_font = pygame.font.Font("gameplay.ttf", 130)
countdown_before_start_content = countdown_before_start_font.render(str(countdown_before_start), True, color["white"])
countdown_before_start_content_rect = countdown_before_start_content.get_rect()
countdown_before_start_content_rect.x = screenwidth/2 - 40
countdown_before_start_content_rect.y = screenheight/2 - 65


# how many seconds last for one number
seconds_each_number = 5
counter = 0

# counter for moving car
counter_for_moving_car = 0

# counter for countdown before next number
counter_for_next_number = 5
counter_for_next_number_font = pygame.font.Font("gameplay.ttf",25)
counter_for_next_number_content = counter_for_next_number_font.render(str(counter_for_next_number),True,color["white"])
counter_for_next_number_content_rect = counter_for_next_number_content.get_rect()
counter_for_next_number_content_rect.x = -200
counter_for_next_number_content_rect.y = -200

# make each element invisible
for each in lst_rect:
    each.x = -200
    each.y = -200

# O, X button
o_button = Button(None, 13, screenwidth / 2 + 120, 550, color["white"], "1", True, True, "o.png")
x_button = Button(None, 13, screenwidth / 2 - 120, 550, color["white"], "1", True, True, "x.png")

# answer list
answer_lst = []
for i in range(len(lst)):
    if i >= 2:
        if lst[i] == lst[i - 2]:
            answer_lst.append("O")
        else:
            answer_lst.append("X")
print(f"answer_lst : {answer_lst}")

# user answer list
user_answer_lst = [" " for _ in range(len(answer_lst))]
print(user_answer_lst)



while run:
    
    update_screen(screen, color["black"])
    # print(pygame.mouse.get_pos())
    # print(main_x_button.rect)
    # Main Menu screen
    if main == True:
        
        if howtoplay == True:
            #print(pygame.mouse.get_pos())
            count_timer = pygame.time.get_ticks()
            screen.blit(matching_number_arrow1.image,(matching_number_arrow1.rect.x, matching_number_arrow1.rect.y))
            screen.blit(matching_number_arrow2.image,(matching_number_arrow2.rect.x, matching_number_arrow2.rect.y))
            screen.blit(count_2back.content, (count_2back.rect.x, count_2back.rect.y))
            screen.blit(count_1back.content, (count_1back.rect.x, count_1back.rect.y))
            
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer
                print(f"countdown : {countdown}")
                countdown_button.content = countdown_button.font_kind.render(str(countdown), True, countdown_button.color)
            
            two_back.draw_text(screen)
            answer_text.draw_text(screen)



            # draw first
            if countdown <= 3:
                n1.draw_text(screen)
            # draw second
            if countdown <= 2:
                n2.draw_text(screen)
            # draw third
            if countdown <= 1:
                n3.draw_text(screen)


            # draw 1-back
            if countdown <= 0:
                matching_number_arrow1.rect.x = 230
                matching_number_arrow1.rect.y = 330
                count_1back.update(230, 370)
            # draw 2- back
            if countdown <= -1:
                matching_number_arrow2.rect.x = 120
                matching_number_arrow2.rect.y = 330
                count_2back.update(120, 370)
            # number moving animation
            if countdown <= -2:
                n1_clone.draw_text(screen)
                n1_clone.rect.x += 3
                n1_clone.rect.y += 2
                if n1_clone.rect.x >= 300:
                    n1_clone.rect.x = 300
                if n1_clone.rect.y >= 430:
                    n1_clone.rect.y = 430
            # color change
            if countdown <= -4:
                n3.color = color["green"]
                n3.content = n3.font_kind.render(n3.text, True, n3.color)
                n1_clone.color = color["green"]
                n1_clone.content = n1_clone.font_kind.render(n1_clone.text, True, n1_clone.color)
            # draw answer
            if countdown <= -5:
                n3_answer.draw_text(screen)
            # delete 1-back, 2-back, and arrows
            if countdown <= -6:
                matching_number_arrow1.update(-200, -200)
                matching_number_arrow2.update(-200, -200)
                count_1back.disappear()
                count_2back.disappear()



            # draw next number
            if countdown <= -7:
                n4.draw_text(screen)
            # draw 1-back
            if countdown <= -8:
                matching_number_arrow1.update(330, 330)
                count_1back.update(330, 370)
            # draw 2-back
            if countdown <= -9:
                matching_number_arrow2.update(230, 330)
                count_2back.update(230, 370)
            # number moving animation
            if countdown <= -10:
                n2_clone.draw_text(screen)
                n2_clone.rect.x += 3
                n2_clone.rect.y += 2
                if n2_clone.rect.x >= 400:
                    n2_clone.rect.x = 400
                if n2_clone.rect.y >= 430:
                    n2_clone.rect.y = 430
            # color change
            if countdown <= -12:
                n2_clone.color = color["grey"]
                n2_clone.content = n2_clone.font_kind.render(n2_clone.text, True, n2_clone.color)
            # draw answer
            if countdown <= - 13:
                n4_answer.draw_text(screen)
            # delete 1-back, 2-back, and arrows
            if countdown <= - 14:
                matching_number_arrow1.update(-200, -200)
                matching_number_arrow2.update(-200, -200)
                count_1back.disappear()
                count_2back.disappear()
                
                

            # draw next number
            if countdown <= -15:
                n5.draw_text(screen)
            # draw 1-back
            if countdown <= -16:
                matching_number_arrow1.update(430, 330)
                count_1back.update(430, 370)
            # draw 2-back
            if countdown <= -17:
                matching_number_arrow2.update(330, 330)
                count_2back.update(330, 370)
            # number moving animation
            if countdown <= -18:
                n3_clone.draw_text(screen)
                n3_clone.rect.x += 3
                n3_clone.rect.y += 2
                if n3_clone.rect.x >= 500:
                    n3_clone.rect.x = 500
                if n3_clone.rect.y >= 430:
                    n3_clone.rect.y = 430
            # color change
            if countdown <= -20:
                n3_clone.color = color["grey"]
                n3_clone.content = n3_clone.font_kind.render(n3_clone.text, True, n3_clone.color)
            # draw answer
            if countdown <= - 21:
                n5_answer.draw_text(screen)
            # delete 1-back, 2-back, and arrows
            if countdown <= - 22:
                matching_number_arrow1.update(-200, -200)
                matching_number_arrow2.update(-200, -200)
                count_1back.disappear()
                count_2back.disappear()




            # draw next number
            if countdown <= -23:
                n6.draw_text(screen)
            # draw 1-back, and 2-back
            if countdown <= -24:
                matching_number_arrow1.update(530, 330)
                count_1back.update(530, 370)
                matching_number_arrow2.update(430, 330)
                count_2back.update(430, 370)

            # number moving animation
            if countdown <= -25:
                n4_clone.draw_text(screen)
                n4_clone.rect.x += 3
                n4_clone.rect.y += 2
                if n4_clone.rect.x >= 600:
                    n4_clone.rect.x = 600
                if n4_clone.rect.y >= 430:
                    n4_clone.rect.y = 430
            # color change
            if countdown <= -27:
                n4_clone.color = color["grey"]
                n4_clone.content = n4_clone.font_kind.render(n4_clone.text, True, n4_clone.color)
            # draw answer
            if countdown <= -28:
                n6_answer.draw_text(screen)
            # delete 1-back, 2-back, and arrows
            if countdown <= -29:
                matching_number_arrow1.update(-200, -200)
                matching_number_arrow2.update(-200, -200)
                count_1back.disappear()
                count_2back.disappear()



            # draw next number
            if countdown <= -30:
                n7.draw_text(screen)
    
            # number moving animation
            if countdown <= -31:
                n5_clone.draw_text(screen)
                n5_clone.rect.x += 3
                n5_clone.rect.y += 2
                if n5_clone.rect.x >= 700:
                    n5_clone.rect.x = 700
                if n5_clone.rect.y >= 430:
                    n5_clone.rect.y = 430
            # color change
            if countdown <= -33:
                n7.color = color["green"]
                n7.content = n7.font_kind.render(n7.text, True, n7.color)
                n5_clone.color = color["green"]
                n5_clone.content = n5_clone.font_kind.render(n5_clone.text, True, n5_clone.color)
            # draw answer
            if countdown <= - 34:
                n7_answer.draw_text(screen)
            # delete 1-back, 2-back, and arrows
            if countdown <= - 35:
                matching_number_arrow1.update(-200, -200)
                matching_number_arrow2.update(-200, -200)
                count_1back.disappear()
                count_2back.disappear()
                n1_clone.disappear()
                n2_clone.disappear()
                n3_clone.disappear()
                n4_clone.disappear()
                n5_clone.disappear()
                

            if countdown <= -40:
                countdown = 3
                n3.color = color["white"]
                n7.color = color["white"]
                n3.content = n3.font_kind.render(n3.text, True, n3.color)
                n7.content = n7.font_kind.render(n7.text, True, n7.color)
                n1_clone.update(100, 300)
                n2_clone.update(200, 300)
                n3_clone.update(300, 300)
                n4_clone.update(400, 300)
                n5_clone.update(500, 300)
                count_1back.disappear()
                count_2back.disappear()
                n1_clone.color = color["white"]
                n2_clone.color = color["white"]
                n3_clone.color = color["white"]
                n4_clone.color = color["white"]
                n5_clone.color = color["white"]
                n1_clone.content = n1_clone.font_kind.render(n1_clone.text, True, n1_clone.color)
                n2_clone.content = n2_clone.font_kind.render(n2_clone.text, True, n2_clone.color)
                n3_clone.content = n3_clone.font_kind.render(n3_clone.text, True, n3_clone.color)
                n4_clone.content = n4_clone.font_kind.render(n4_clone.text, True, n4_clone.color)
                n5_clone.content = n5_clone.font_kind.render(n5_clone.text, True, n5_clone.color)
                

                


           
            howtoplay_title_button.draw_text(screen)
            howtoplay_back_button.draw_text(screen)

            howtoplay_title_button.hovered(color['green'], 32, color['white'], 32, handshape = False)
            
            howtoplay_back_button.hovered(color['green'], 42, color['white'], 42, False)

            if howtoplay_back_button.check_click():
                
                # game control - howtoplay menu exit
                howtoplay = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        print("backspace key pressed")
                        main_x_button.content = main_x_button.font_kind.render(main_x_button.text, True, color['white'])
                        howtoplay = False

        elif credit == True:

            credit_title_button.draw_text(screen)
            credit_made_by_button.draw_text(screen)
            credit_back_button_button.draw_text(screen)
            
            credit_title_button.hovered(color['green'], 42, color['white'], 42, False, x = credit_title_button.rect.x, y = credit_title_button.rect.y)
            credit_made_by_button.hovered(color['green'], 64, color['white'], 64, False, x = credit_made_by_button.rect.x, y = credit_made_by_button.rect.y)

            credit_back_button_button.hovered(color['green'], 42, color['white'], 42, False, x = credit_back_button_button.rect.x, y = credit_back_button_button.rect.y)


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
                        main_x_button.content = main_x_button.font_kind.render(main_x_button.text, True, color['white'])
                        credit = False
            
        else:

            main_mainmenu_button.draw_text(screen)
            main_start_button.draw_text(screen)
            main_howtoplay_button.draw_text(screen)
            main_credit_button.draw_text(screen)
            main_exit_button.draw_text(screen)
            main_x_button.draw_text(screen)

            main_start_button.hovered(color['green'], 42, color['white'], 32, True, True, main_start_button.rect.x, main_start_button.rect.y)
            main_howtoplay_button.hovered(color['green'], 36, color['white'], 32, False, 250, 320)
            main_credit_button.hovered(color['green'], 32, color['white'], 32, False)
            main_exit_button.hovered((130,130,130), 25, color['white'], 32, False)

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
        update_screen(screen,color["black"])

        pygame.draw.line(screen,color["white"],(100,150),(700,150),2)
        screen.blit(start_image,(120,92))
        screen.blit(finish_image,(630,88))
        screen.blit(car_image,(car_image_rect.x, car_image_rect.y))

        # blit images from lst_rendered_contents onto screen
        for i in range(len(lst_rendered_contents)):
            screen.blit(lst_rendered_contents[i], lst_rect[i])
        

        # every 0.2 second - before start
        current_count = pygame.time.get_ticks()

        if current_count - last_count > 200:
            countdown_before_start += 0.2
            last_count = current_count
            countdown_before_start_content = countdown_before_start_font.render(str(countdown_before_start), True, color["white"])
            quotient = int(countdown_before_start) // 5
            rem = int(countdown_before_start) % 5
            

            #print(round(countdown_before_start,2)%5)
            if countdown_before_start < 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                countdown_before_start_content = countdown_before_start_font.render(str(int(-countdown_before_start)), True, color["white"])
            
            elif int(countdown_before_start) == 0:
                countdown_before_start_content = countdown_before_start_font.render(str("Start!"), True, color["white"])
                countdown_before_start_content_rect.x = screenwidth/2 - 260
            
            elif 0 < countdown_before_start < len(lst_rect) * 5 :
                countdown_before_start_content_rect.center = -200, -200
                lst_rect[quotient - 1].center = -200, -200
                counter_for_next_number_content_rect.x = 680
                counter_for_next_number_content_rect.y = 20
                
                # every 5 second car moves
                if round(countdown_before_start,2) % 5 == 0.0:
                    car_image_rect.x += 600/number_of_questions
                
                # this makes number disappear for a short time
                if quotient*5 + 4.78 < countdown_before_start:
                    lst_rect[quotient].center = -200, -200
                else:
                    lst_rect[quotient].center = screenwidth / 2, screenheight / 2 - 100
            
            #print(round(countdown_before_start,2))

            if 0 <= countdown_before_start < number_of_questions * 5 :
                if rem == 0:
                    counter_for_next_number_content = counter_for_next_number_font.render(" ",True,color["white"])
                if rem == 1:
                    counter_for_next_number_content = counter_for_next_number_font.render(" ",True,color["white"])
                if rem == 2:
                    counter_for_next_number_content = counter_for_next_number_font.render("3",True,color["white"])
                if rem == 3:
                    counter_for_next_number_content = counter_for_next_number_font.render("2",True,color["white"])
                if rem == 4:
                    counter_for_next_number_content = counter_for_next_number_font.render("1",True,color["white"])

            elif round(countdown_before_start,2) >= number_of_questions * 5:
                counter_for_next_number_content = counter_for_next_number_font.render(" ",True,color["white"])
                
        
        if 10.0 <= round(countdown_before_start, 2) <= 5 * number_of_questions:
            o_button.draw_text(screen)
            x_button.draw_text(screen)
            o_button.hovered(None, 12)
            x_button.hovered(None, 12)
            answer_submitted = False
            

            if o_button.check_click():
                print(f"quotient - 2 : {quotient-2}")
                user_answer_lst[quotient-2] = "O"
                print(user_answer_lst)
                print("o clicked")
                print(f"current number:{lst[quotient]}")
                print(f"2-back number:{lst[quotient - 2]}")
                
                if lst[quotient] == lst[quotient - 2]:
                    print("correct choice!")
                else:
                    print("wrong choice!")

            if x_button.check_click():
                user_answer_lst[quotient-2] = "X"
                print(user_answer_lst)
                print("x clicked")
                print(f"current number:{lst[quotient]}")
                print(f"2-back number:{lst[quotient - 2]}")
                
                if lst[quotient] != lst[quotient - 2]:
                    print("correct choice!")
                else:
                    print("wrong choice!")
        


        screen.blit(counter_for_next_number_content,(counter_for_next_number_content_rect.x, counter_for_next_number_content_rect.y))
        screen.blit(countdown_before_start_content,(countdown_before_start_content_rect.x, countdown_before_start_content_rect.y))


    allow_to_exit_program()

    pygame.display.flip()
    fps_clock.tick(fps)
