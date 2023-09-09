import numpy as np 
from turtle import t
class drawSomething:

    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.edges = list(transition_matrix.keys())

    def get_next_line(self, current_edge):
        return np.random.choice (self.edges,p= [self.transition_matrix[current_edge][next_edge] for next_edge in self.edges])

    def draw(self, next_edge):

        self.edges.append(next_edge)
        return self.edges 


def main():

    drawing = drawSomething({  
        
        "Red": {"A": 0.2, "B": 0.5, "C": .03},
		"Blue": {"A": 0.7, "B": 0.2, "C": .01},
		"Green": {"A": 0.3, "B": 0.4, "C": .03}

    })


if "__name__" == "__main__":
    main()

