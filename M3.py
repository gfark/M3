import numpy as np 
from turtle import * 
import turtle

print(1)

ANGLES = {

    "black": 45,
    "blue": 150,
    "orange" : 130,
    
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
                
                t.forward(250)


            
            else:
                t.right(coord[1]) 
                t.forward(100)

            
                            
    

        
    
def main():

    drawing = drawSomething({  
        
        "black": {"black": 0.1, "blue": 0.5, "orange": .4},
		"blue": {"black": 0.1, "blue": 0.8, "orange": .1},
		"orange": {"black": 0.2, "blue": 0.1, "orange": .7}

    })

    to_draw = drawing.drawing_sequence(current_color="blue", line_number=100)
    drawing.draw(to_draw)
    
    


if __name__ == "__main__":
    main()

