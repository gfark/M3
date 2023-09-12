import numpy as np 
from turtle import * 

print(1)

ANGLES = {

    "red": 30,
    "blue": 45,
    "purple" : 130
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

        print("step 2")
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
        print(sequence)

        
        t = Turtle()


        for coord in sequence:
            t.color(coord[0])
            t.right(coord[1])
            t.forward(100)

        
    
def main():

    drawing = drawSomething({  
        
        "red": {"red": 0.2, "blue": 0.5, "purple": .3},
		"blue": {"red": 0.7, "blue": 0.2, "purple": .1},
		"purple": {"red": 0.1, "blue": 0.3, "purple": .6}

    })

    to_draw = drawing.drawing_sequence(current_color="red", line_number=100)
    drawing.draw(to_draw)
    
    


if __name__ == "__main__":
    main()

