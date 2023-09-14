import numpy as np 
from turtle import * 
import turtle
from random import *


ANGLES = {

    "black": 45,
    "blue": 150,
    "orange" : 155,
    "pink": 152.5
    
}


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
            current_edge 
        """
        
        temp = np.random.choice (self.edges,p= [self.transition_matrix[current_edge][next_edge] for next_edge in self.edges])
        
        return temp
    
    def get_next_angle(self, current_color="red"):
        """
        Retrieves the next angle based off the color chosen
        Args:
            current_color (string): color name
        """

    
        angle = ANGLES.get(current_color)
        return angle


    def drawing_sequence(self, current_color="red", line_number=20):
        """
        Put the color and angle combination together in order to draw
        """

        drawing_order = []
        while len(drawing_order) < line_number:

            next_color = self.get_next_color(current_color)
            current_angle = self.get_next_angle(current_color)
            coordinate = [current_color, current_angle]
            current_color = next_color
            drawing_order.append(coordinate)
        
        return drawing_order


    def draw(self, sequence):
        
    
        t = Turtle()
        turtle.Screen().bgcolor("black")
        turtle.screensize(900, 700)
        turn = 0
        for coord in sequence:
            
            t.color(coord[0])
            
            if coord[1] == 45:
                if turn == 0:
                    t.right(coord[1])
                    turn = 1
                else:
                    t.left(coord[1])
                    turn = 0   
                
                if t.xcor() > 900 or t.xcor() < -900:
                    x = randint(-900,900)
                    y = randint(-900, 900)
                    t.setpos(x,y)
                
                if t.ycor() > 700 or t.ycor() < -700:
                    x = randint(-700,700)
                    y = randint(-700, 700)
                    t.setpos(x,y)
                    
                

            
                t.forward(250)

            else:
                t.right(coord[1]) 
                t.forward(100)


            
        turtle.Screen().exitonclick() 

            
                
    
def main():

    drawing = drawSomething({  
        
        "black": {"black": 0.1, "blue": 0.4, "orange": 0.3, "pink": 0.2},
		"blue": {"black": 0.1, "blue": 0.7, "orange": 0.1, "pink": 0.1},
		"orange": {"black": 0.1, "blue": 0.3, "orange": 0.4, "pink": 0.2},
        "pink": {"black": 0.1, "blue": 0.2, "orange": 0.2, "pink": 0.5}

    })

    to_draw = drawing.drawing_sequence(current_color="blue", line_number=200)
    drawing.draw(to_draw)
    
    


if __name__ == "__main__":
    main()

