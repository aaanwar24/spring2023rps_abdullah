# File created by Abdullah Anwar 

# the objective of this code is to create an interactive game of rock, paper, scissors, with images as well as rules. 
# time give us access to the sleep function, which allows us to slow the code down 
# random allows the computer to make a decision on whether it wants to choose and play rock, paper, or scissors. 
# pygame is where we get graphics 
# the operating system allows the program to find files in the computer. 
# game_folder tells the program where in the computer to find a certain file. 

from time import sleep 
from random import randint 
import pygame as pg 
import os 
game_folder = os.path.dirname(__file__)
print(game_folder)

# these game settings define the size of the playing window 
WIDTH = 800
HEIGHT = 800
FPS = 30

# define colors
# tuples are immutable - you cannot change the value once created 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# this defines the different choices for integers that can be selected 
# from the list. 0 corresponds to rock, 1 to paper, and 2 to scissors. 
choices = ["rock", "paper", "scissors"]

# the draw_text function tells the computer to draw text in a certain 
# size, font, and in a specific place. 
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# the cpu_randchoice function allows the computer to randomly pick 
# a value that corresponds to the choices defined above. 
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice



# first the program initializes pygame, and basically turns it on. It gets pygame ready to use the pixels on the screen 
# kind  of like a light switch 
# the program then opens pygame in a window that is defined by set_mode under the paramters for WIDTH and HEIGHT that have been defined previously 
# when you open up the window, it has a caption on the top, and this gives the string values for the caption. 
# Clock is a class that does a few things, and it ticks at frames per second. 

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("rock, paper, scissors...")
clock = pg.time.Clock()

# rock_image creates the variable that stores the pixels and keeps them as ready to be used. 
# rock_image_rect isn't storing the pixels themselves, but the dimensions of the pixels, and allows us to access and change those things. 
# if you add to the rock_image_rect variable, it will move. Adding or subtratcing to x and y in certain quantities will lead
# the image to move in a variety of directions
# you need rect because it allows you to change the location of a function 
# the same is done for the paper and scissors images
# after importing the images for the player choices, the program imports 
# the image for the cpu to use for the variable cpu_choice 


rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()


scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = rock_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()


# running is a variable and it hold the value of True. It remains true until labelled as false like. 
running = True
home =True 
restart = False 
player_choice = ""
cpu_choice = ""

'''
This next block of code is essentially the entire game. Let's split it up into 
parts. first we defineevents. An event is any time that something happens to the computer that 
causes them to run a loop. Next we establish flow control. flow control 
drop us out of the loop and brings us all the way to the pg.quit and ends 
the loop. If the coordinates of the mouse collide with the coordinates of 
an image, the program prints that an image has been selected, after which it 
proceeds to pick a random of the three through the function cpu_randchoice. 


'''

while running:
    clock.tick(FPS) 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            print(pg.mouse.get_pos()[0])
            print(pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock..")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper...")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors...")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()                      
            else:
                print("you didn't click on anything...")

        
    '''
    This is where the program draw the images on the screen, after it has 
    been given the instructions on what to do when a certain image is selected. 
    After that, the program uses the draw_text function to tell the user to 
    input their choice. 
    '''
    screen.fill(BLACK)
    screen.blit(rock_image, rock_image_rect)
    rock_image_rect.y = 200
    screen.blit(paper_image, paper_image_rect)
    paper_image_rect.y = 600
    screen.blit(scissors_image, scissors_image_rect)
    draw_text("choose rock, paper, or scissors", 22, WHITE, WIDTH/2, HEIGHT/10)

    '''
    The remaining portion of the code is the comparison of the user choice and 
    the cpu choice. It gives the instructions of what to print, a win, loss, or tie,
    depending on what the user and cpu picked. After the comparison, the program 
    displays that the tab must be closed and replayed to start a new game. 
    '''
    if player_choice == "rock":
        screen.fill(BLACK)
        screen.blit(rock_image, rock_image_rect)
        rock_image_rect.y = 200
        


        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           
            
        elif cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("Loser!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           
          
            
        elif cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("Winner!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           
            
    
    if player_choice == "paper":
        screen.fill(BLACK)
        screen.blit(paper_image, paper_image_rect)
        paper_image_rect.y = 600

        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           
            

        elif cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("Winner!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           
            
        elif cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("Loser!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           


    if player_choice == "scissors":
        screen.fill(BLACK) 
        screen.blit(scissors_image, scissors_image_rect)

        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           
            
            
        elif cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("Winner!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           
            
            
        elif cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("Loser!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("close tab to play again", 22, WHITE, WIDTH/2, HEIGHT/5)
           
            
    pg.display.flip()


pg.quit

pg.quit
    
    

