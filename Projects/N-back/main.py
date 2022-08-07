
import pygame
from object import Object
from random import randint,choice

pygame.init()

pygame.display.set_caption("N-Back")





##### Settings #####
# icon
icon = pygame.image.load("n.png")
pygame.display.set_icon(icon)

# fps
fps = 60
clock = pygame.time.Clock()
  
# color
color = {"black" : (0,0,0),"white":(255,255,255),"green":(0,255,0),
         "grey":(175,173,169),"red":(255,0,0),"light green":(144,238,144),
         "sky blue": (50,130,230)
         }

# FPS
fps_clock = pygame.time.Clock()
fps = 60

# Count down timer
countdown = 4
last_count = pygame.time.get_ticks()
last_count2 = pygame.time.get_ticks()

# current N-back
current_nback = 2


# Questions (numbers)
lst = []
lst_rendered_contents = []
lst_rect = []
lst_answer = []
lst_rendered_contents_2 = []

number_of_questions = 4

# Background

# Main menu
bg1 = pygame.image.load("bg1.png")
bg2 = pygame.image.load("bg2.png")
bg3 = pygame.image.load("bg3.png")
bg4 = pygame.image.load("bg4.png")
bg8 = pygame.image.load("bg8.png")
scroll2 = 0
scroll3 = 0
scroll4 = 0
bg2_width = bg2.get_width()
bg3_width = bg3.get_width()
bg4_width = bg4.get_width()

# Game screen
gamebg = pygame.image.load("bgspace.png")
scroll5 = 0
gamebg_width = gamebg.get_width()


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
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()



################################## Game Control ###################################

# Random number generator control
random_number_control = False

# Ultimate control - to exit the game
run = True

# Main Menu

# Main Menu control - to exit the main menu
main = True

# How to play menu control - to exit the how to play menu
howtoplay = False

# Credit menu control - to exit the credit menu
credit = False

# Options menu control - to exit the options menu
options = False

# Gameplay screen
game = False

# Score screen
score = False
score_update_control = False

# sound control
number_appear_sound_flag = False
count_down_sound_flag = False
game_start_sound_flag = False
game_background_sound_flag = False
clock_tick_sound_flag =False


percentage_control = False

#################################################################################



def regenerate_numbers():
    global lst, number_of_questions, random_number_control, lst_rect, lst_rendered_contents,lst_answer, lst_user_answer
    
    if random_number_control == False:
        random_number_control = True
        font = pygame.font.Font("gameplay.ttf", 164)
        for i in range(number_of_questions):
            lst.append(randint(1,9))
            each_content_1 = font.render(str(lst[i]), True, color["white"])
            each_rect_1 = each_content_1.get_rect()
            lst_rendered_contents.append(each_content_1)
            lst_rect.append(each_rect_1)
        print(f"{current_nback}-back, {lst}")
        
        # answer list
        lst_answer = []
        for i in range(len(lst)):
            if i >= current_nback:
                if lst[i] == lst[i - current_nback]:
                    lst_answer.append("O")
                else:
                    lst_answer.append("X")
        print(f"lst_answer : {lst_answer}")

        # user answer list
        lst_user_answer = [" " for _ in range(len(lst_answer))]
        print(lst_user_answer)

        # make each element invisible
        for each in lst_rect:
            each.x = -200
            each.y = -200

        

def play_sound(filename, volume = 1, loop = False):
    sound = pygame.mixer.Sound(filename)
    if volume != 1:
        sound.set_volume(volume)
    if loop:
        sound.play(-1)
    else:
        sound.play()

def reset_all_sound_flags():
    global number_appear_sound_flag,count_down_sound_flag,game_start_sound_flag,game_background_sound_flag,clock_tick_sound_flag
    number_appear_sound_flag = False
    count_down_sound_flag = False
    game_start_sound_flag = False
    game_background_sound_flag = False
    clock_tick_sound_flag =False


# buttons
class Button:
    
    def __init__(self, font_name, size, x, y, color, text, center = False, image = False, imagefile_name = None):
        self.click_sound = pygame.mixer.Sound("click.wav")
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
            #print("hovered")
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
            #print("hovered2")
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

    def left_right_movement(self):
        self.left_key_pressed = False
        self.right_key_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left key pressed")
                    self.left_key_pressed = True
                    return self.left_key_pressed
                if event.key == pygame.K_RIGHT:
                    print("right key pressed")
                    self.right_key_pressed = True
                    return self.right_key_pressed



    def key_movement(self):
        global main

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.click_sound.set_volume(0.8)
                if event.key == pygame.K_UP:
                    print("up key pressed")
                    self.rect.y -= self.move
                    self.click_sound.play()
                if event.key == pygame.K_DOWN:
                    print("down key pressed")
                    self.rect.y += self.move
                    self.click_sound.play()
                if event.key == pygame.K_RETURN:
                    print("Enter key pressed")
                    return True
                if event.key == pygame.K_BACKSPACE:
                    print("Backspace key pressed")
                    self.click_sound.play()
                if main == True:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.move = 0
                if event.key == pygame.K_DOWN:
                    self.move = 0
        
            self.move = 100

    def disappear(self):
        self.rect.center = -2000,-2000
    
    def update_position(self,x,y):
        self.rect.x = x
        self.rect.y = y






        

"""From here is instantiations and calling functions """

# Create screen
create_screen(800,800)


# Main Menu buttons
main_mainmenu_button = Button("8bitwonder.ttf", 84, screenwidth / 2, 100, color['white'], "N Back", True)
main_start_button = Button("8bitwonder.ttf", 32, screenwidth / 2, 220, color['white'], "Start", True)
main_howtoplay_button = Button("8bitwonder.ttf", 32, screenwidth / 2, 320, color['white'], "How to play", True)
main_credit_button = Button("8bitwonder.ttf", 32, screenwidth / 2, 420, color['white'], "Credit", True)
main_options_button = Button("8bitwonder.ttf",32,screenwidth/2,520,color["white"],"Options",True)
main_exit_button = Button("8bitwonder.ttf", 32, screenwidth / 2, 620, color['white'], "Exit", True)

# Main Menu key scroll X
main_x_button = Button("8bitwonder.ttf", 24, screenwidth / 2 - 200, 0, color['white'], "*", False)


# How to play buttons
howtoplay_title_button = Button("8bitwonder.ttf", 32, 250, 220, color['white'], "How to play")
howtoplay_back_button = Button("8bitwonder.ttf", 42, 250, 520, color['white'], "Back")

howtoplay_title_button.rect.center = screenwidth / 2, screenheight / 2 - 300
howtoplay_back_button.rect.center = screenwidth / 2, screenheight / 2 + 300

# countdown - how to play menu
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

two_back = Button("8bitwonder.ttf", 42, screenwidth / 2, 190, color["green"], "2 Back", True)
questions_text = Button("8bitwonder.ttf", 28, 50, 250, color["white"],"questions")
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


# Credit Menu buttons
credit_title_button = Button("8bitwonder.ttf", 42, 250, 220, color['white'], "Credit")
credit_made_by_button = Button("8bitwonder.ttf", 64, 250, 320, color['white'], "Jinsung Kim")
credit_back_button = Button("8bitwonder.ttf", 42, 250, 520, color['white'], "Back")

credit_title_button.rect.center = screenwidth / 2, screenheight / 2 - 200
credit_made_by_button.rect.center = screenwidth / 2, screenheight / 2 - 100
credit_back_button.rect.center = screenwidth / 2, screenheight / 2 + 200

# Option menu buttons
options_title_button = Button("8bitwonder.ttf",42,screenwidth / 2, screenheight / 2 - 300,color["white"],"Options",True)
options_n_back_text = Button("gameplay.ttf",32,150,250,color["white"],"# n",True)
options_number_of_questions_text1 = Button("8bitwonder.ttf",20,150,400,color["white"],"number",True)
options_number_of_questions_text2 = Button("8bitwonder.ttf",20,150,430,color["white"],"of",True)
options_number_of_questions_text3 = Button("8bitwonder.ttf",20,150,460,color["white"],"questions",True)

options_2back = Button("8bitwonder.ttf",32,360,250,color["white"],"2",True)
options_3back = Button("8bitwonder.ttf",32,440,250,color["white"],"3",True)
options_4back = Button("8bitwonder.ttf",32,520,250,color["white"],"4",True)
options_5back = Button("8bitwonder.ttf",32,600,250,color["white"],"5",True)
options_6back = Button("8bitwonder.ttf",32,680,250,color["white"],"6",True)

options_low_number_of_questions = Button("8bitwonder.ttf",20,350,430,color["white"],"Low",True)
options_med_number_of_questions = Button("8bitwonder.ttf",20,530,430,color["white"],"Med",True)
options_high_number_of_questions = Button("8bitwonder.ttf",20,710,430,color["white"],"High",True)

options_back_button = Button("8bitwonder.ttf",42,250,520,color["white"],"Back")
options_back_button.rect.center = screenwidth / 2, screenheight / 2 + 200

options_key = Object(5,5,32,3,1,True,False)
options_key.rect.center = 357,280


########################## Buttons & objects in Game screen#############################

# current n-back status
current_nback_text_font = pygame.font.Font("8bitwonder.ttf",20)
current_nback_text_content = current_nback_text_font.render(str(current_nback) + " Back",True,color["white"])

# start, finish, car, dashboard images
earth_image = Object(110,90,50,50,1,False,True,"earth.png")
space_station_image = Object(640,78,50,50,1,False,True,"spacestation.png")
rocket_image = Object(110,80,50,50,1,center = False,does_image_exist=True,imagefile_name="rocket.png")
odometer_image = Object(screenwidth/2,600,100,100,1,True,True,"speedometer.png")
screen_image = Object(screenwidth/2,600,100,100,1,True,True,"tablet.png")

# countdown before start
countdown_before_start = -4
countdown_before_start_font = pygame.font.Font("gameplay.ttf", 130)
countdown_before_start_content = countdown_before_start_font.render(str(countdown_before_start), True, color["white"])
countdown_before_start_content_rect = countdown_before_start_content.get_rect()
countdown_before_start_content_rect.x = screenwidth/2 - 40
countdown_before_start_content_rect.y = screenheight/2 - 60


# how many seconds last during one number
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


# O, X button
o_button = Button(None, 13, screenwidth / 2 + 120, 530, color["white"], "1", True, True, "o.png")
x_button = Button(None, 13, screenwidth / 2 - 120, 530, color["white"], "1", True, True, "x.png")


#########################################################################################



# score screen


rectangle_outside = pygame.rect.Rect(50,40,700,700)
result_text = Button("8bitwonder.ttf",55,screenwidth/2,100,color["white"],"Result",True)
n_back_text = Button("gameplay.ttf",20,165,210,color["white"],"n-back",True)
questions = Button("gameplay.ttf",20,165,280,color["white"],"questions",True)
correct_answers = Button("gameplay.ttf",20,165,420,color["white"],"correct answer",True)
user_answers = Button("gameplay.ttf",20,165,560,color["white"],"your answer",True)
result_percentage_text = Button("gameplay.ttf",20,165,650,color["white"],"Score",True)
go_back_to_main_menu_button = Button("gameplay.ttf",20,190,692,color["white"],"Press enter key to go to Main menu")

number_of_correct_questions = 0

n_back_answer = Button("gameplay.ttf",20,520,210,color["white"],str(current_nback),True)



def update_score():
    global lst_rendered_contents_2,score_update_control

    if score_update_control == False:
        score_update_control = True
        for each_n in lst:
            each_number_font = pygame.font.Font("gameplay.ttf", 20)
            each_number_content = each_number_font.render(str(each_n), True, color["white"])
            lst_rendered_contents_2.append(each_number_content)


while run:
    
    update_screen(screen, color["sky blue"])

    # Main Menu screen
    if main == True:
        
        for i in range(3):
            screen.blit(bg2,(bg2_width * i + scroll2,0))
        for i in range(3):
            screen.blit(bg3,(bg3_width * i + scroll3,0))
        for i in range(3):
            screen.blit(bg4,(bg4_width * i + scroll4,0))
        scroll2 -= 0.5
        scroll3 -= 1
        scroll4 -= 2
        if abs(scroll2)>bg2_width:
            scroll2 = 0
        if abs(scroll3)>bg3_width:
            scroll3 = 0
        if abs(scroll4)>bg4_width:
            scroll4 = 0

        screen.blit(bg8,(0,150))
        if howtoplay == True:
            
            count_timer = pygame.time.get_ticks()
            screen.blit(matching_number_arrow1.image,(matching_number_arrow1.rect.x, matching_number_arrow1.rect.y))
            screen.blit(matching_number_arrow2.image,(matching_number_arrow2.rect.x, matching_number_arrow2.rect.y))
            screen.blit(count_2back.content, (count_2back.rect.x, count_2back.rect.y))
            screen.blit(count_1back.content, (count_1back.rect.x, count_1back.rect.y))
            
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer
                #print(f"countdown : {countdown}")
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
                count_1back.update_position(230, 370)
            # draw 2- back
            if countdown <= -1:
                matching_number_arrow2.rect.x = 120
                matching_number_arrow2.rect.y = 330
                count_2back.update_position(120, 370)
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
                matching_number_arrow1.update_position(-200, -200)
                matching_number_arrow2.update_position(-200, -200)
                count_1back.disappear()
                count_2back.disappear()



            # draw next number
            if countdown <= -7:
                n4.draw_text(screen)
            # draw 1-back
            if countdown <= -8:
                matching_number_arrow1.update_position(330, 330)
                count_1back.update_position(330, 370)
            # draw 2-back
            if countdown <= -9:
                matching_number_arrow2.update_position(230, 330)
                count_2back.update_position(230, 370)
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
                matching_number_arrow1.update_position(-200, -200)
                matching_number_arrow2.update_position(-200, -200)
                count_1back.disappear()
                count_2back.disappear()
                
                

            # draw next number
            if countdown <= -15:
                n5.draw_text(screen)
            # draw 1-back
            if countdown <= -16:
                matching_number_arrow1.update_position(430, 330)
                count_1back.update_position(430, 370)
            # draw 2-back
            if countdown <= -17:
                matching_number_arrow2.update_position(330, 330)
                count_2back.update_position(330, 370)
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
                matching_number_arrow1.update_position(-200, -200)
                matching_number_arrow2.update_position(-200, -200)
                count_1back.disappear()
                count_2back.disappear()




            # draw next number
            if countdown <= -23:
                n6.draw_text(screen)
            # draw 1-back, and 2-back
            if countdown <= -24:
                matching_number_arrow1.update_position(530, 330)
                count_1back.update_position(530, 370)
                matching_number_arrow2.update_position(430, 330)
                count_2back.update_position(430, 370)

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
                matching_number_arrow1.update_position(-200, -200)
                matching_number_arrow2.update_position(-200, -200)
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
                matching_number_arrow1.update_position(-200, -200)
                matching_number_arrow2.update_position(-200, -200)
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
                n1_clone.update_position(100, 300)
                n2_clone.update_position(200, 300)
                n3_clone.update_position(300, 300)
                n4_clone.update_position(400, 300)
                n5_clone.update_position(500, 300)
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
                

                


            questions_text.draw_text(screen)
            howtoplay_title_button.draw_text(screen)
            howtoplay_back_button.draw_text(screen)

            howtoplay_title_button.hovered(color['green'], 32, color['white'], 32, handshape = False)
            
            howtoplay_back_button.hovered(color['green'], 42, color['white'], 42, False)

            if howtoplay_back_button.check_click():
                play_sound("back.wav",0.8)
                # game control - howtoplay menu exit
                howtoplay = False
                # I set this because if I click the back button, it also clicks exit button in main menu
                pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        print("backspace key pressed")
                        main_x_button.content = main_x_button.font_kind.render(main_x_button.text, True, color['white'])
                        howtoplay = False
                        play_sound("back.wav",0.8)

        elif credit == True:

            credit_title_button.draw_text(screen)
            credit_made_by_button.draw_text(screen)
            credit_back_button.draw_text(screen)
            
            credit_title_button.hovered(color['green'], 42, color['white'], 42, False, x = credit_title_button.rect.x, y = credit_title_button.rect.y)
            credit_made_by_button.hovered(color['green'], 64, color['white'], 64, False, x = credit_made_by_button.rect.x, y = credit_made_by_button.rect.y)

            credit_back_button.hovered(color['green'], 42, color['white'], 42, False, x = credit_back_button.rect.x, y = credit_back_button.rect.y)


            if credit_back_button.check_click():
                play_sound("back.wav",0.8)
                print("back button clicked")
                credit = False
                # I set this because if I click the back button, it also clicks exit button in main menu
                pygame.time.delay(100)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        print("backspace key pressed")
                        credit = False
                        play_sound("back.wav",0.8)
        
        elif options == True:
            #print(pygame.mouse.get_pos())
            pygame.draw.rect(screen, color["white"], options_key)
            options_title_button.draw_text(screen)
            options_back_button.draw_text(screen)
            options_n_back_text.draw_text(screen)
            options_number_of_questions_text1.draw_text(screen)
            options_number_of_questions_text2.draw_text(screen)
            options_number_of_questions_text3.draw_text(screen)
            options_2back.draw_text(screen)
            options_3back.draw_text(screen)
            options_4back.draw_text(screen)
            options_5back.draw_text(screen)
            options_6back.draw_text(screen)
            options_low_number_of_questions.draw_text(screen)
            options_med_number_of_questions.draw_text(screen)
            options_high_number_of_questions.draw_text(screen)
            options_2back.hovered(color["white"],32,color["white"],32,True)
            options_3back.hovered(color["white"],32,color["white"],32,True)
            options_4back.hovered(color["white"],32,color["white"],32,True)
            options_5back.hovered(color["white"],32,color["white"],32,True)
            options_6back.hovered(color["white"],32,color["white"],32,True)
            options_low_number_of_questions.hovered(color["white"],20,color["white"],20,True)
            options_med_number_of_questions.hovered(color["white"],20,color["white"],20,True)
            options_high_number_of_questions.hovered(color["white"],20,color["white"],20,True)

            if options_2back.check_click():
                current_nback = 2
                if number_of_questions <= 2:
                    number_of_questions = 3
                play_sound("sci.wav",0.8)
            if options_3back.check_click():
                current_nback = 3
                if number_of_questions <= 3:
                    number_of_questions = 4
                play_sound("sci.wav",0.8)
            if options_4back.check_click():
                current_nback = 4
                if number_of_questions <= 4:
                    number_of_questions = 5
                play_sound("sci.wav",0.8)
            if options_5back.check_click():
                current_nback = 5
                if number_of_questions <= 5:
                    number_of_questions = 6
                play_sound("sci.wav",0.8)
            if options_6back.check_click():
                current_nback = 6
                if number_of_questions <= 6:
                    number_of_questions = 7
                play_sound("sci.wav",0.8)
            if current_nback == 2:
                options_2back.content = options_2back.font_kind.render("2",True,color["green"])
                options_3back.content = options_3back.font_kind.render("3",True,color["white"])
                options_4back.content = options_4back.font_kind.render("4",True,color["white"])
                options_5back.content = options_5back.font_kind.render("5",True,color["white"])
                options_6back.content = options_6back.font_kind.render("6",True,color["white"])
            elif current_nback == 3:
                options_2back.content = options_2back.font_kind.render("2",True,color["white"])
                options_3back.content = options_3back.font_kind.render("3",True,color["green"])
                options_4back.content = options_4back.font_kind.render("4",True,color["white"])
                options_5back.content = options_5back.font_kind.render("5",True,color["white"])
                options_6back.content = options_6back.font_kind.render("6",True,color["white"])
            elif current_nback == 4:
                options_2back.content = options_2back.font_kind.render("2",True,color["white"])
                options_3back.content = options_3back.font_kind.render("3",True,color["white"])
                options_4back.content = options_4back.font_kind.render("4",True,color["green"])
                options_5back.content = options_5back.font_kind.render("5",True,color["white"])
                options_6back.content = options_6back.font_kind.render("6",True,color["white"])
            elif current_nback == 5:
                options_2back.content = options_2back.font_kind.render("2",True,color["white"])
                options_3back.content = options_3back.font_kind.render("3",True,color["white"])
                options_4back.content = options_4back.font_kind.render("4",True,color["white"])
                options_5back.content = options_5back.font_kind.render("5",True,color["green"])
                options_6back.content = options_6back.font_kind.render("6",True,color["white"])
            elif current_nback == 6:
                options_2back.content = options_2back.font_kind.render("2",True,color["white"])
                options_3back.content = options_3back.font_kind.render("3",True,color["white"])
                options_4back.content = options_4back.font_kind.render("4",True,color["white"])
                options_5back.content = options_5back.font_kind.render("5",True,color["white"])
                options_6back.content = options_6back.font_kind.render("6",True,color["green"])
            
            if options_low_number_of_questions.check_click():
                number_of_questions = current_nback + choice(range(2,5))
                print(f"number_of_questions:{number_of_questions}")
                print(f"current n_back : {current_nback}")
                play_sound("clicks.wav",0.8)
            elif options_med_number_of_questions.check_click():
                number_of_questions = current_nback + choice(range(5,9))
                print(f"number_of_questions:{number_of_questions}")
                print(f"current n_back : {current_nback}")
                play_sound("clicks.wav",0.8)
            elif options_high_number_of_questions.check_click():
                number_of_questions = current_nback + choice(range(9,13))
                print(f"number_of_questions:{number_of_questions}")
                print(f"current n_back : {current_nback}")
                play_sound("clicks.wav",0.8)

            if 2 <= number_of_questions - current_nback <= 4:
                options_low_number_of_questions.content = options_low_number_of_questions.font_kind.render("low",True,color["green"])
                options_med_number_of_questions.content = options_med_number_of_questions.font_kind.render("med",True,color["white"])
                options_high_number_of_questions.content = options_high_number_of_questions.font_kind.render("high",True,color["white"])
            elif 5 <= number_of_questions - current_nback <= 8:
                options_low_number_of_questions.content = options_low_number_of_questions.font_kind.render("low",True,color["white"])
                options_med_number_of_questions.content = options_med_number_of_questions.font_kind.render("med",True,color["green"])
                options_high_number_of_questions.content = options_high_number_of_questions.font_kind.render("high",True,color["white"])
            elif 9 <= number_of_questions - current_nback <= 12:
                options_low_number_of_questions.content = options_low_number_of_questions.font_kind.render("low",True,color["white"])
                options_med_number_of_questions.content = options_med_number_of_questions.font_kind.render("med",True,color["white"])
                options_high_number_of_questions.content = options_high_number_of_questions.font_kind.render("high",True,color["green"])
            


            options_back_button.hovered(color["green"],options_back_button.size,color["white"],options_back_button.size,handshape = False)
            if options_back_button.check_click():
                options = False
                play_sound("back.wav",0.8)
                # I set this because if I click the back button, it also clicks exit button in main menu
                pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        print("backspace key pressed")
                        options = False
                        play_sound("back.wav",0.8)
                    if event.key == pygame.K_LEFT:
                        play_sound("menuclick.wav",0.8)
                        if options_key.rect.y < 300:
                            options_key.rect.x -= 80
                        else:
                            options_key.rect.x -= 180
                        
                    if event.key == pygame.K_RIGHT:
                        play_sound("menuclick.wav",0.8)
                        if options_key.rect.y < 300:
                            options_key.rect.x += 80
                        else:
                            options_key.rect.x += 180
                        
                    if event.key == pygame.K_UP:
                        play_sound("menuclick.wav",0.8)
                        options_key.rect.y -= 180
                        options_key.rect.width = 32
                    if event.key == pygame.K_DOWN:
                        play_sound("menuclick.wav",0.8)
                        if options_key.rect.y < 300:
                            options_key.rect.y += 180
                        options_key.rect.width = 64
                        options_key.rect.x = 315

                    if event.key == pygame.K_RETURN:
                        
                        if 260 < options_key.rect.y < 300:
                            play_sound("sci.wav",0.8)
                            if 340 < options_key.rect.x < 380:
                                current_nback = 2
                                if number_of_questions <= 2:
                                    number_of_questions = 3
                            if 420 < options_key.rect.x < 460:
                                current_nback = 3
                                if number_of_questions <= 3:
                                    number_of_questions = 4
                            if 500 < options_key.rect.x < 540:
                                current_nback = 4
                                if number_of_questions <= 4:
                                    number_of_questions = 5
                            if 580 < options_key.rect.x < 620:
                                current_nback = 5
                                if number_of_questions <= 5:
                                    number_of_questions = 6
                            if 660 < options_key.rect.x < 700:
                                current_nback = 6
                                if number_of_questions <= 6:
                                    number_of_questions = 7
                        if 455 < options_key.rect.y < 475:
                            play_sound("clicks.wav",0.8)
                            if 305 < options_key.rect.x < 325:
                                number_of_questions = current_nback + choice(range(2,5))
                            if 485 < options_key.rect.x < 505:
                                number_of_questions = current_nback + choice(range(5,9))
                            if 665 < options_key.rect.x < 685:
                                number_of_questions = current_nback + choice(range(9,13))
                            print(f"number_of_questions:{number_of_questions}")
                            print(f"current n_back : {current_nback}")

                    
            if options_key.rect.y < 360:
                if options_key.rect.x <= 341:
                    options_key.rect.x = 341
                if options_key.rect.x >= 661:
                    options_key.rect.x = 661
                if options_key.rect.y <= 280:
                    options_key.rect.y = 280
 
            elif 450 < options_key.rect.y < 470:
                if options_key.rect.x <= 315:
                    options_key.rect.x = 315
                if options_key.rect.x >=675:
                    options_key.rect.x = 675
                if options_key.rect.y >= 460:
                    options_key.rect.y = 460
            

                        

        else:

            main_mainmenu_button.draw_text(screen)
            main_start_button.draw_text(screen)
            main_howtoplay_button.draw_text(screen)
            main_credit_button.draw_text(screen)
            main_options_button.draw_text(screen)
            main_exit_button.draw_text(screen)
            main_x_button.draw_text(screen)

            main_start_button.hovered(color['green'], 32, color['white'], 32, True, True, main_start_button.rect.x, main_start_button.rect.y)
            main_howtoplay_button.hovered(color['green'], 32, color['white'], 32, False, 250, 320)
            main_credit_button.hovered(color['green'], 32, color['white'], 32, False)
            main_options_button.hovered(color["green"],32,color["white"],32,False)
            main_exit_button.hovered((130,130,130), 25, color['white'], 32, False)

            if main_start_button.check_click():
                play_sound("gamestart.ogg")
                print("start menu clicked")
                game = True
                main = False
            if main_credit_button.check_click():
                play_sound("entersound.wav",0.8)
                print("credit menu clicked")
                credit = True
            if main_howtoplay_button.check_click():
                play_sound("entersound.wav",0.8)
                print("how to play menu clicked")
                howtoplay = True
            if main_options_button.check_click():
                play_sound("entersound.wav",0.8)
                print("options menu clicked")
                options = True
            if main_exit_button.check_click():
                run = False
            
            if main_x_button.key_movement():
                
                if main_x_button.rect.y < 250:
                    print("START!!!")
                    game = True
                    main = False
                    play_sound("gamestart.ogg")
                elif main_x_button.rect.y < 350:
                    print("HOW TO PLAY pressed")
                    howtoplay = True
                    play_sound("entersound.wav",1)
                elif main_x_button.rect.y < 450:
                    print("CREDIT pressed")
                    credit = True
                    play_sound("entersound.wav",1)
                elif main_x_button.rect.y < 550:
                    print("Option pressed")
                    options = True
                    play_sound("entersound.wav",1)
                elif main_x_button.rect.y < 650:
                    print("EXIT pressed")
                    run = False

            if main_x_button.rect.y < 208:
                main_x_button.rect.y = 208
            if main_x_button.rect.y < 250:
                main_x_button.rect.x = 284
            if 290 < main_x_button.rect.y <350:
                main_x_button.rect.x = 195
            if 390 < main_x_button.rect.y < 450:
                main_x_button.rect.x = 276
            if 490 < main_x_button.rect.y < 550:
                main_x_button.rect.x = 261
            if 590 < main_x_button.rect.y < 650:
                main_x_button.rect.x = 310
            if main_x_button.rect.y > 608:
                main_x_button.rect.y = 608
    
    # Game screen
    elif game == True:
        main = False
        update_screen(screen,color["black"])
        
        screen.blit(gamebg,(0,0))
        odometer_image.transform_image(1.2,1)
        odometer_image.draw_on_screen(screen,100,660)
        screen_image.transform_image(1.3,1.5)
        screen_image.draw_on_screen(screen,75,-80)
        regenerate_numbers()
        current_nback_text_content = current_nback_text_font.render(str(current_nback)+" Back",True,color["white"])
        screen.blit(current_nback_text_content,(110,240))
        earth_image.draw_on_screen(screen,100,82)
        space_station_image.draw_on_screen(screen,640,78)
        rocket_image.draw_on_screen(screen,rocket_image.rect.x,rocket_image.rect.y)
        
        #print(pygame.mouse.get_pos())

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
            
            if int(countdown_before_start) < 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                countdown_before_start_content = countdown_before_start_font.render(str(int(-countdown_before_start)), True, color["white"])
                if int(countdown_before_start) == -3:
                    if count_down_sound_flag == False:
                        count_down_sound_flag = True
                        play_sound("countdown.wav")

            elif int(countdown_before_start) == 0 :
                countdown_before_start_content = countdown_before_start_font.render(str("Start!"), True, color["white"])
                countdown_before_start_content_rect.x = screenwidth/2 - 260
                if game_start_sound_flag == False:
                    game_start_sound_flag = True
                    play_sound("countdown_start.wav",volume=0.8)
                
            
            if 0 < countdown_before_start < len(lst_rect) * 5 :
                countdown_before_start_content_rect.center = -200, -200
                lst_rect[quotient - 1].center = -200, -200
                counter_for_next_number_content_rect.x = 680
                counter_for_next_number_content_rect.y = 20
                rocket_image.rect.x += 500/number_of_questions/25


                # every 5 second car moves
                # if round(countdown_before_start,2) % 5 == 0.0:
                #     rocket_image_rect.x += 500/number_of_questions
                

                # this makes number disappear for a short time
                if quotient*5 + 4.78 < countdown_before_start:
                    lst_rect[quotient].center = -200, -200
                else:
                    lst_rect[quotient].center = screenwidth / 2 + 10, screenheight / 2 - 45


            # show counter before the next number shows up - used remainder
            if 0 <= countdown_before_start < number_of_questions * 5 :
                
                if game_background_sound_flag == False:
                    game_background_sound_flag = True
                    pygame.mixer.music.load("game_loop_background.wav")
                    pygame.mixer.music.set_volume(3)
                    pygame.mixer.music.play(-1) 

                if rem == 0:
                    if number_appear_sound_flag == False:
                        number_appear_sound_flag = True
                        play_sound("number_appear.mp3")
                    counter_for_next_number_content = counter_for_next_number_font.render(" ",True,color["white"])
                    
                if rem == 1:
                    counter_for_next_number_content = counter_for_next_number_font.render(" ",True,color["white"])
                    number_appear_sound_flag = False
                if rem == 2:
                    counter_for_next_number_content = counter_for_next_number_font.render("3",True,color["white"])
                    if clock_tick_sound_flag == False:
                        clock_tick_sound_flag = True
                        play_sound("clock_tick.wav")
                if rem == 3:
                    clock_tick_sound_flag = False
                    counter_for_next_number_content = counter_for_next_number_font.render("2",True,color["white"])
                if rem == 4:
                    counter_for_next_number_content = counter_for_next_number_font.render("1",True,color["white"])
                    

            elif round(countdown_before_start,2) >= number_of_questions * 5:
                counter_for_next_number_content = counter_for_next_number_font.render(" ",True,color["white"])


        if 5 * current_nback <= round(countdown_before_start, 2) < 5 * number_of_questions:
            o_button.draw_text(screen)
            x_button.draw_text(screen)
            o_button.hovered(None, 12)
            x_button.hovered(None, 12)
            
            # I tried to implement left key for 'X', and right key for 'O' but it didn't let me
            # so I am just using only x button to determine left key pressed or right key pressed.
            x_button.left_right_movement()


            if o_button.check_click() or x_button.right_key_pressed:
                print(f"quotient - 2 : {quotient-current_nback}")
                lst_user_answer[quotient-current_nback] = "O"
                print(lst_user_answer)
                print("o clicked")
                print(f"current number:{lst[quotient]}")
                print(f"current_nback-back number:{lst[quotient - current_nback]}")
                play_sound("mouseclick.wav",volume = 0.5)
                if lst[quotient] == lst[quotient - current_nback]:
                    print("correct choice!")
                else:
                    print("wrong choice!")

            if x_button.check_click() or x_button.left_key_pressed:
                lst_user_answer[quotient-current_nback] = "X"
                print(lst_user_answer)
                print("x clicked")
                print(f"current number:{lst[quotient]}")
                print(f"current_nback-back number:{lst[quotient - current_nback]}")
                play_sound("mouseclick.wav",volume = 0.5)
                if lst[quotient] != lst[quotient - current_nback]:
                    print("correct choice!")
                else:
                    print("wrong choice!")
        
        #print(round(countdown_before_start,2))
        if round(countdown_before_start,2) > number_of_questions * 5:
            pygame.mixer.music.fadeout(1500)
            reset_all_sound_flags()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
            score = True
            game = False
            
        screen.blit(counter_for_next_number_content,(counter_for_next_number_content_rect.x, counter_for_next_number_content_rect.y))
        screen.blit(countdown_before_start_content,(countdown_before_start_content_rect.x, countdown_before_start_content_rect.y))

        #print(f"round(countdown_before_start,2):{round(countdown_before_start,2)}")

    elif score == True:
        game = False
        screen.fill(color["black"])
        
        # this allows to reset the previous score and update_position new result
        update_score()

        pygame.draw.rect(screen, color["white"], rectangle_outside, 3)
        pygame.draw.line(screen,color["white"], (100,150), (700,150), 2)
        pygame.draw.line(screen,color["white"], (280,200), (280,680), 2)

        #screen.blit(earth_image,(120,92))
        earth_image.draw_on_screen(screen,100,82)
        space_station_image.draw_on_screen(screen,640,78)
        rocket_image.rotate_image(90)
        rocket_image.draw_on_screen(screen,600,rocket_image.rect.y)
        screen.blit(result_text.content, result_text.rect)
        
        n_back_text.draw_text(screen)
        questions.draw_text(screen)
        correct_answers.draw_text(screen)
        user_answers.draw_text(screen)
        n_back_answer.draw_text(screen)
        n_back_answer.content = n_back_answer.font_kind.render(str(current_nback),True,color["white"])
        result_percentage_text.draw_text(screen)
        go_back_to_main_menu_button.draw_text(screen)
        go_back_to_main_menu_button.hovered(color['green'],20, color['white'], 20, handshape = True)
        
        # questions 
        if len(lst_rendered_contents_2) <= 10:
            for index, each in enumerate(lst_rendered_contents_2):
                screen.blit(each, ((280 + (470 * (index + 1) / (len(lst_rendered_contents_2) + 1))), 270))
        
        elif len(lst_rendered_contents_2) > 10:
            number_of_lines = len(lst_rendered_contents_2) // 10
            for index, each in enumerate(lst_rendered_contents_2):
                if index <= 9:
                    screen.blit(each, ((280 + (470 * (index + 1) / (11))), 270))
                if 9 < index <= 19:
                    screen.blit(each, ((280 + (470 * (index%10 + 1) / (11))), 270 + 40))
                if 19 < index:
                    screen.blit(each, ((280 + (470 * (index%10 + 1) / (11))), 270 + 80))
        

        # correct answer 
        if len(lst_answer) <= 10:
            for index, each in enumerate(lst_answer):
                answer_font = pygame.font.Font("gameplay.ttf",20)
                answer_content = answer_font.render(str(each),True,color["white"])
                screen.blit(answer_content,((280 + (470 * (index + 1) / (len(lst_answer) + 1))), 410))
 
        elif len(lst_answer) > 10:
            for index, each in enumerate(lst_answer):
                answer_font = pygame.font.Font("gameplay.ttf",20)
                answer_content = answer_font.render(str(each),True,color["white"])

                if index <= 9:
                    screen.blit(answer_content, ((280 + (470 * (index + 1) / (11))), 410))
                if 9 < index <= 19:
                    screen.blit(answer_content, ((280 + (470 * (index%10 + 1) / (11))), 410 + 40))
                if 19 < index:
                    screen.blit(answer_content, ((280 + (470 * (index%10 + 1) / (11))), 410 + 80))

        # user answer
        if len(lst_user_answer) <= 10:
            for index, each in enumerate(lst_user_answer):
                user_answer_font = pygame.font.Font("gameplay.ttf",20)
                if each == " ":
                    each = "n/a"
                    user_answer_font = pygame.font.Font("gameplay.ttf",10)
                user_answer_content = user_answer_font.render(str(each),True,color["white"])
                screen.blit(user_answer_content,((280 + (470 * (index + 1) / (len(lst_user_answer) + 1))), 540))
        elif len(lst_user_answer) > 10:
            for index, each in enumerate(lst_user_answer):
                user_answer_font = pygame.font.Font("gameplay.ttf",20)
                if each == " ":
                    each = "n/a"
                    user_answer_font = pygame.font.Font("gameplay.ttf",10)
                user_answer_content = user_answer_font.render(str(each),True,color["white"])
                if index <= 9:
                    screen.blit(user_answer_content, ((280 + (470 * (index + 1) / (11))), 540))
                if 9 < index <= 19:
                    screen.blit(user_answer_content, ((280 + (470 * (index % 10 + 1) / (11))), 540 + 40))
                if 19 < index:
                    screen.blit(user_answer_content, ((280 + (470 * (index % 10 + 1) / (11))), 540 + 80))

        if percentage_control == False:
            percentage_control = True
            for i in range(len(lst_answer)):
                if lst_answer[i] == lst_user_answer[i]:
                    number_of_correct_questions += 1
            percentage = number_of_correct_questions / len(lst_answer) * 100
        percentage_font = pygame.font.Font("gamecube.ttf",20)
        percentage_message = percentage_font.render(str(round(percentage,2)) + " %",True, color["white"])
        if percentage >= 80:
            percentage_message = percentage_font.render(str(round(percentage,2)) + " %",True, color["green"])
        elif percentage <= 40:
            percentage_message = percentage_font.render(str(round(percentage,2)) + " %",True, color["red"])
        percentage_message_rect = percentage_message.get_rect()
        percentage_message_rect.center = 525, 645
        screen.blit(percentage_message,percentage_message_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    last_count = 0
                    current_count = 0
                    countdown_before_start = -4
                    score_update_control = False
                    percentage_control = False
                    rocket_image.rect.x = 110
                    rocket_image.rect.y = 80
                    countdown_before_start_content_rect.x = screenwidth/2 - 40
                    countdown_before_start_content_rect.y = screenwidth/2 - 60
                    number_of_correct_questions = 0
                    for i in range(len(lst_rendered_contents)):
                        lst_rendered_contents.pop(0)
                        lst.pop(0)
                        lst_rendered_contents_2.pop(0)
                    for i in range(len(lst_answer)):
                        lst_answer.pop(0)
                        lst_user_answer.pop(0)
                    random_number_control = False
                    screen.fill(color["black"])
                    rocket_image.flag = False
                    rocket_image.rotate_image(270)
                    rocket_image.flag = False
                    main = True
                    score = False
        if go_back_to_main_menu_button.check_click():
            last_count = 0
            current_count = 0
            countdown_before_start = -4
            score_update_control = False
            percentage_control = False
            rocket_image.rect.x = 110
            rocket_image.rect.y = 80
            countdown_before_start_content_rect.x = screenwidth/2 - 40
            countdown_before_start_content_rect.y = screenwidth/2 - 60
            number_of_correct_questions = 0
            for i in range(len(lst_rendered_contents)):
                lst_rendered_contents.pop(0)
                lst.pop(0)
                lst_rendered_contents_2.pop(0)
            for i in range(len(lst_answer)):
                lst_answer.pop(0)
                lst_user_answer.pop(0)
            random_number_control = False
            screen.fill(color["black"])
            rocket_image.flag = False
            rocket_image.rotate_image(270)
            rocket_image.flag = False
            main = True
            score = False
        
        


    allow_to_exit_program()

    pygame.display.flip()
    fps_clock.tick(fps)
