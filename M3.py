import numpy as np 
from turtle import * 
import turtle
from random import *

"""
Author: Greta Farkas
Course: Computations Creativity- CSCI 3725
Assignment: M3 Markov Distinction
Date: 9/14/23
Description: 
The file draws a night sky with stars based of an inputed color,
and number of lines, which results in the number stars drawn.
It contains the class drawSomething, which takes in a transition matrix of colors,
to predicts the next move. The colors have corresponding angles which 
aid in creating different styles of stars.



"""


ANGLES = {

    "black": 45,
    "yellow": 150,
    "orange" : 155,
    "pink": 152.5
    
}

"""
Class drawSomething:

Functions:
__init__ , get_next_color, get_next_angle, drawing_sequence, draw

Description: 
Contains functions that draw and aid in drawing a night sky with stars
based off a probabiltiy matrix
"""
class drawSomething:

    def __init__(self, transition_matrix):
        """
        Simulates a person drawing a person
        Args:
            transition_matrix (dict): transition probabilities  
        """
        self.transition_matrix = transition_matrix
        self.edges = list(transition_matrix.keys())
        

    def get_next_color(self, current_edge):
        """
        Decides the next line to draw based off the current line
        Args:
            current_edge (): takes in the current color being used from the transition matric
        """
        
        temp = np.random.choice (self.edges,p= [self.transition_matrix[current_edge][next_edge] for next_edge in self.edges])
        
        return temp
    
    def get_next_angle(self, current_color="red"):
        """
        Retrieves angle corresponding to the color chosen
        Args:
            current_color (string): color name
        """

    
        angle = ANGLES.get(current_color)
        return angle


    def drawing_sequence(self, current_color="red", line_number=20):
        """
        Puts the color and angle combination in a list and adds that list to the drawings
        sequence order
        Args:
            current_color (string): decides the inital color in the transition matrix to start with
            line_number (int): input # of lines to include in the drawing

        """
        #list to store the sequence predicted
        drawing_order = []


        while len(drawing_order) < line_number:

            #retrieves the next color from the transition matrix
            next_color = self.get_next_color(current_color)

            #retrieves the star corner angle based of the color
            current_angle = self.get_next_angle(current_color)

            #creates the angle and color pairing 
            coordinate = [current_color, current_angle]

            #sets the current colors as the next color
            current_color = next_color

            #adds the angle color pairing to the drawing sequence list
            drawing_order.append(coordinate)
        
        return drawing_order


    def draw(self, current_color="yellow", line_number=200):
        """
        Function that draws the stars in the night sky and initiates the drawing
        Args:
            current_color (string): inital color in the probability matrix to start at
            line_number (int): number of lines to be included in the stars 
        """

        #retreives the list of moves for the turtle to make
        sequence = self.drawing_sequence(current_color, line_number)
    
        #sets up the popup screen
        t = Turtle()
        turtle.Screen().bgcolor("black")
        turtle.screensize(900, 700)
        t.speed(10)
        t.ht()
        
        #initalizes variables that tell the turtle when to turn left and right
        turn = 0
        count = 0
        for coord in sequence:
            
            #sets the turtle color
            t.color(coord[0])
            
            #if statement with specific directions for when the tranisition matrix is black and is starting
            #to creat a new star
            if coord[1] == 45:
                
                t.penup()
                
                #if turn is 0, the turtle turns right after two turns
                if turn == 0:
                    t.right(coord[1])
                    count += 1
                    if count == 2:
                        turn = 1
                        count = 0

                #if the turn is 1, the turtle turns left after two turns     
                else:
                    t.left(coord[1])
                    count += 1
                    if count == 2:
                        turn = 0
                        count = 0
                      
                #makes sure the turtle stays within the bounds of the screen
                if t.xcor() > 300 or t.xcor() < -300:
                    x = randint(-300,300)
                    y = randint(-300, 300)

                    t.setpos(x,y)
                
                if t.ycor() > 100 or t.ycor() < -100:
                    x = randint(-100,100)
                    y = randint(-100, 100)
                    t.setpos(x,y)
                    
        
                t.forward(300)
                t.pendown()

            else:
                t.right(coord[1]) 
                t.forward(100)


            
        turtle.Screen().exitonclick() 

            
                
    
def main():

    drawing = drawSomething({  
        
        "black": {"black": 0.0, "yellow": 0.3, "orange": 0.4, "pink": 0.3},
		"yellow": {"black": 0.1, "yellow": 0.7, "orange": 0.0, "pink": 0.2},
		"orange": {"black": 0.1, "yellow": 0.2, "orange": 0.7, "pink": 0.0},
        "pink": {"black": 0.1, "yellow": 0.0, "orange": 0.2, "pink": 0.7}

    })


    drawing.draw("yellow", 200)
    
    


if __name__ == "__main__":
    main()

