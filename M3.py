import numpy as np 
from turtle import * 


ANGLES = {

    "red": 30,
    "blue": 45,
    "yellow" : 90
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
        """
        temp = np.random.choice (self.edges,p= [self.transition_matrix[current_edge][next_edge] for next_edge in self.edges])

        print(temp)

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

        

    def draw(self, next_edge):

        self.edges.append(next_edge)
        return self.edges 
    
    
def main():

    drawing = drawSomething({  
        
        "red": {"A": 0.2, "B": 0.5, "C": .03},
		"blue": {"A": 0.7, "B": 0.2, "C": .01},
		"yellow": {"A": 0.3, "B": 0.4, "C": .03}

    })


if "__name__" == "__main__":
    main()

