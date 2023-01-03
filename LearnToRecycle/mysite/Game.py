'''
Created on Nov 12, 2022

Interactive Game to Help teach 
how to dispose of household objects.

@author: rayan
'''
import pygame 
import sys
import sqlite3
from tkinter import *

pygame.init()  
white = (255, 255, 255)  
# assigning values to height and width variable   
height = 1300 
width = 760
# creating the display surface object   
# of specific dimension..e(X, Y).   
display_surface = pygame.display.set_mode((height, width))  
  
# set the pygame window name   
pygame.display.set_caption('Learn to Recycle')  
  
# creating a surface object, image is drawn on it.   
image = pygame.image.load(r'Labels Above.jpg')  
dest = (432, 521)
answer_dest = (350,280)

correct = pygame.font.SysFont('Corbel',200).render('Correct!' , True , white)
wrong = pygame.font.SysFont('Corbel',200).render('Try Again' , True , white)
game_over = pygame.font.SysFont('Corbel',200).render('Game Over :)' , True , white)


index = 0
conn = sqlite3.connect('TrashList.db')
cursor = conn.execute("SELECT * FROM TrashList")
list_items = []
list_bin = []
for row in cursor:
    list_items.append(row[0])
    list_bin.append(row[2])
    
def init():
    global index
    
    display_surface.blit(image, (0, 0))
    
    item_text = pygame.font.SysFont('Corbel',100).render(list_items[index] , True , white)
    display_surface.blit(item_text, dest)
    
    for event in pygame.event.get():  

        mouse = pygame.mouse.get_pos();
        #cursor by recycle
        if 200 <= mouse[0] <= 400 and 200 <= mouse[1] <= 400:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if list_bin[index] == 1:
                    index = index + 1
                    screen = pygame.display.get_surface()
                    screen.blit(screen, (0, 0))
                    screen.fill(pygame.Color("green")) # erases the entire screen surface
                    screen.blit(screen, (0, 0)) 
                    display_surface.blit(correct,answer_dest)
                    pygame.display.update() 
                    pygame.time.delay(2000)
                    pygame.display.flip() 
                else:
                    screen = pygame.display.get_surface()
                    screen.blit(screen, (0, 0))
                    screen.fill(pygame.Color("red")) # erases the entire screen surface
                    screen.blit(screen, (0, 0)) 
                    display_surface.blit(wrong,answer_dest)
                    pygame.display.update() 
                    pygame.time.delay(2000)
                    pygame.display.flip()
                
        #cursor over compost
        if 500 <= mouse[0] <= 800 and 200 <= mouse[1] <= 400:
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if list_bin[index] == 2:
                    index = index + 1
                    screen = pygame.display.get_surface()
                    screen.blit(screen, (0, 0))
                    screen.fill(pygame.Color("green")) # erases the entire screen surface
                    screen.blit(screen, (0, 0)) 
                    display_surface.blit(correct,answer_dest)
                    pygame.display.update() 
                    pygame.time.delay(2000)
                    pygame.display.flip() 
                else:
                    screen = pygame.display.get_surface()
                    screen.blit(screen, (0, 0))
                    screen.fill(pygame.Color("red")) # erases the entire screen surface
                    screen.blit(screen, (0, 0)) 
                    display_surface.blit(wrong,answer_dest)
                    pygame.display.update() 
                    pygame.time.delay(2000)
                    pygame.display.flip()
        #cursor over trash
        if 900 <= mouse[0] <= 1100 and 200 <= mouse[1] <= 400:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if list_bin[index] == 0:
                    index = index + 1
                    screen = pygame.display.get_surface()
                    screen.blit(screen, (0, 0))
                    screen.fill(pygame.Color("green")) # erases the entire screen surface
                    screen.blit(screen, (0, 0)) 
                    display_surface.blit(correct,answer_dest)
                    pygame.display.update() 
                    pygame.time.delay(2000)
                    pygame.display.flip()
                else: 
                    screen = pygame.display.get_surface()
                    screen.blit(screen, (0, 0))
                    screen.fill(pygame.Color("red")) # erases the entire screen surface
                    screen.blit(screen, (0, 0)) 
                    display_surface.blit(wrong,answer_dest)
                    pygame.display.update() 
                    pygame.time.delay(2000)
                    pygame.display.flip()
        
        if index == 18:
            screen = pygame.display.get_surface()
            screen.blit(screen, (0, 0))
            screen.fill(pygame.Color("orange")) # erases the entire screen surface
            screen.blit(screen, (0, 0)) 
            display_surface.blit(game_over,(200,280))
            pygame.display.update() 
            pygame.time.delay(10000)
            pygame.display.flip()
            pygame.quit()
            
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()  
        # Draws the surface object to the screen.   
        pygame.display.update()   
    

def gameloop():
    """ The main loop to run the game """
    while True:
        init()
gameloop()
    
