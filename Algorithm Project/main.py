# main.py
import tkinter as tk
from graph import Graph
from design import GraphDesign

# Example usage:

# Creating an instance of the Graph class with 10 vertices.
graph = Graph(10)

# Creating a random graph using the create_random_graph method.
random_graph = graph.create_random_graph()

# Creating the main window for the GUI.
window = tk.Tk()

# Create an instance of the GraphDesign class
graph_design = GraphDesign(window, random_graph)

# Running the main event loop for the GUI.
window.mainloop()
