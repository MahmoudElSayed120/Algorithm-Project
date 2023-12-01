import tkinter as tk
import random

class GraphDesign:
    def __init__(self, window, graph):
        self.window = window
        self.graph = graph
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Dijkstra's Algorithm")

        # Creating a canvas to display the map.
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="lightgray")
        self.canvas.pack()

        # Creating a dictionary to store the coordinates of each vertex on the map.
        self.vertex_coordinates = {}

        # Calculating the coordinates for each vertex on the map.
        for i in range(self.graph.vertices):
            x = random.randint(50, 750)
            y = random.randint(50, 550)
            self.vertex_coordinates[i] = (x, y)

        # Drawing the edges on the map.
        for i in range(self.graph.vertices):
            for j in range(i + 1, self.graph.vertices):
                if self.graph.adjacency_matrix[i][j] != 0:
                    x1, y1 = self.vertex_coordinates[i]
                    x2, y2 = self.vertex_coordinates[j]
                    self.canvas.create_line(x1, y1, x2, y2, width=2, fill="black")

        # Drawing the vertices on the map.
        for i in range(self.graph.vertices):
            x, y = self.vertex_coordinates[i]
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white", outline="black")
            self.canvas.create_text(x, y, text=str(i), fill="black")

        # Creating labels and entry fields for the start and end vertices.
        input_frame = tk.Frame(self.window, bg="lightgray")
        input_frame.pack(pady=10)

        start_label = tk.Label(input_frame, text="Start Vertex:", bg="lightgray", font=("Helvetica", 12))
        start_label.grid(row=0, column=0, padx=5, pady=5)
        self.start_entry = tk.Entry(input_frame, font=("Helvetica", 12))
        self.start_entry.grid(row=0, column=1, padx=5, pady=5)

        end_label = tk.Label(input_frame, text="End Vertex:", bg="lightgray", font=("Helvetica", 12))
        end_label.grid(row=1, column=0, padx=5, pady=5)
        self.end_entry = tk.Entry(input_frame, font=("Helvetica", 12))
        self.end_entry.grid(row=1, column=1, padx=5, pady=5)

        # Creating a button to find the shortest path.
        find_button = tk.Button(self.window, text="Find Shortest Path", command=self.find_shortest_path, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        find_button.pack(pady=10)

        # Creating a label to display the result.
        self.result_label = tk.Label(self.window, text="", bg="lightgray", font=("Helvetica", 12, "bold"))
        self.result_label.pack()

    def find_shortest_path(self):
        start_vertex = self.start_entry.get()
        end_vertex = self.end_entry.get()

        # Input validation
        if not start_vertex.isdigit() or not end_vertex.isdigit():
            self.result_label.config(text="Invalid input. Please enter valid vertex values.", fg="red")
            return

        start_vertex, end_vertex = int(start_vertex), int(end_vertex)

        if start_vertex < 0 or start_vertex >= self.graph.vertices or end_vertex < 0 or end_vertex >= self.graph.vertices:
            self.result_label.config(text="Invalid start or end vertex.", fg="red")
            return

        shortest_path = self.graph.dijkstra(start_vertex, end_vertex)
        self.result_label.config(text="Shortest Path: " + " -> ".join(map(str, shortest_path)), fg="blue")

        # Animate the path
        self.animate_path(shortest_path)

    def animate_path(self, path):
        """
        Animate the traversal of the shortest path on the graph.
        """
        if not path:
            return

        # Extracting coordinates for each vertex in the path.
        path_coordinates = [self.vertex_coordinates[vertex] for vertex in path]

        # Recursive function for animation.
        def animate(index):
            if index < len(path_coordinates) - 1:
                x1, y1 = path_coordinates[index]
                x2, y2 = path_coordinates[index + 1]
                self.canvas.create_line(x1, y1, x2, y2, width=2, fill="red")
                self.window.after(1000, animate, index + 1)  # 1000 milliseconds (1 second) delay
            else:
                # Reset the canvas after animation is complete.
                self.visualize_graph()

        # Start the animation with the first edge.
        animate(0)

    def visualize_graph(self):
        """
        Visualizes the graph using the visualize_graph method from the Graph class.
        """
        # Reset the canvas to remove previous visualizations.
        self.canvas.delete("all")

        # Drawing the edges on the map.
        for i in range(self.graph.vertices):
            for j in range(i + 1, self.graph.vertices):
                if self.graph.adjacency_matrix[i][j] != 0:
                    x1, y1 = self.vertex_coordinates[i]
                    x2, y2 = self.vertex_coordinates[j]
                    self.canvas.create_line(x1, y1, x2, y2, width=2, fill="black")

        # Drawing the vertices on the map.
        for i in range(self.graph.vertices):
            x, y = self.vertex_coordinates[i]
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white", outline="black")
            self.canvas.create_text(x, y, text=str(i), fill="black")
