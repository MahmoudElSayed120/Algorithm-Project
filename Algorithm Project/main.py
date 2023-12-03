import tkinter as tk
from graph import Graph
from design import GraphDesign

if __name__ == "__main__":
    # Create a graph instance
    graph = Graph(vertices=28, node_names=[
        "Beirut", "Tripoli", "Akkar", "Jezzine", "Zahla", "Rashaya",
        "Anout", "Sidon", "Barja", "Naqoura", "Aley", "Hemmana",
        "Baabda", "Bet ed Dine"
    ])

    # Create the main window and run the application
    window = tk.Tk()
    graph_design = GraphDesign(window, graph)
    window.mainloop()
