# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:45:53 2022

@author: BangTheBanger
"""

################################
####Module Initialization#######
################################
import pygame, random
pygame.init()


################################
####Variable Initialization#####
################################
#Screen Width and Height
#CAN CHANGE
width = 1000
#CAN CHANGE
height = 800
#
screen = pygame.display.set_mode([width,height])


#background color for fill function
#CAN CHANGE
BLACK = (0,0,0)


#make True to cover trails
#CAN CHANGE
notrails = False


#amount of circles
#CAN CHANGE
ciramount = 100


#speed of the circles, first value is horizontal speed, second is vertical
#CAN CHANGE
speed = [2, 1]


#list of circles. Each circle is a list. it goes as:
    #circles[circlenumber][circlecolor][circlelocation][circleradius]
circles = [[(0, 0, 0), [0, 0], (0)]]*ciramount

################################
####Circle Initialization#######
################################
for i in range(ciramount):
    #variable to decide how many of the circles are black
    randchance = random.randint(0,10)
    
    
    
    #this decides the chance of the circle being black. 6 means 60% chance
    #CAN CHANGE
    chancecutoff = 6
    
    #this if decides if the circle is black
    if randchance <= chancecutoff:
        colortobe = (0,0,0)
    
    
    
    #the else defines what color it should be if not black
    else:
        #cyan rain
        colortobe = (random.randint(0,10), random.randint(254,255), random.randint(254,255))
    
        #color rain
        #colortobe = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
    
    
    #initializes each circle with random values
    circles[i] = [
                         colortobe                                                       #Color index 0
                        , [random.randint(-width,width), random.randint(-height,height)] #Location index 1
                        , (random.randint(5,20))                                         #Radius index 2
                 ]




timer = pygame.time.Clock()

keepGoing = True


################################
####Main Loop###################
################################
while keepGoing:
    
    #quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    
    
    #cover trails function
    if(notrails):
        screen.fill(BLACK)
    
    
    
    
    #redrawing the circle in the new location
    for i in range(ciramount):
        
        #initialize the circle variables to change position
        circolor     = circles[i][0]
        cirlocation  = circles[i][1]
        cirradius    = circles[i][2]
        
        #draw circle in new position
        pygame.draw.circle(screen, circolor, cirlocation, cirradius)
        
        
        #change position of the circle
        circles[i][1][0] += speed[0]
        circles[i][1][1] += speed[1]
        
        
        #Loops the circles when they get out of bounds
        if circles[i][1][0] >= width:
            circles[i][1][0] = -width
        
        if circles[i][1][1] >= height:
            circles[i][1][1] = -height
    
    
    
    
    #update display and set refresh rate, I have a 240hz monitor, set it to your preferred speed.
    pygame.display.update()
    timer.tick(240)
    
pygame.quit()
