# design.py

import tkinter as tk

class GraphDesign:
    # Define node coordinates at the class level
    node_coordinates = {
        "Beirut": (350, 265),
        "Tripoli": (450, 70),
        "Sidon": (320, 435),
        "Anout": (470, 375),
        "Akkar": (450, 40),
        "Jezzine": (400, 435),
        "Zahla": (550, 265),
        "Rashaya": (550, 435),
        "Barja": (350, 345),
        "Naqoura": (250, 570),
        "Aley": (455, 225),
        "Hemmana": (465, 265),
        "Baabda": (400, 265),
        "Bet ed Dine": (470, 335)
    }

    def __init__(self, window, graph):
        self.window = window
        self.graph = graph
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Dijkstra's Algorithm")

        # Creating a canvas to display the map with a background image.
        self.canvas = tk.Canvas(self.window, width=1000, height=600)
        self.canvas.pack()

        # Load the background image
        background_image = tk.PhotoImage(file='Lebanon.png')
        self.canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

        # Adding a reference to the background image to prevent it from being garbage collected
        self.canvas.background_image = background_image

        # Drawing the edges on the map.
        for i in range(self.graph.vertices):
            for j in range(i + 1, self.graph.vertices):
                if self.graph.adjacency_matrix[i][j] != 0:
                    x1, y1 = self.node_coordinates[self.graph.index_to_node_name(i)]
                    x2, y2 = self.node_coordinates[self.graph.index_to_node_name(j)]
                    self.canvas.create_line(x1, y1, x2, y2, width=2, fill="black")

        # Drawing the vertices on the map.
        for node_name, (x, y) in self.node_coordinates.items():
            self.canvas.create_rectangle(x - 40, y - 10, x + 40, y + 10, fill="white", outline="black", tags=node_name)
            self.canvas.create_text(x, y, text=node_name, fill="black", tags=node_name)

            # Bind click event to each node
            self.canvas.tag_bind(node_name, '<Button-1>', lambda event, name=node_name: self.node_clicked(name))

        # Creating labels and entry fields for the start and end vertices.
        input_frame = tk.Frame(self.window, bg="lightgray")
        input_frame.pack(pady=10)

        start_label = tk.Label(input_frame, text="Start Node:", bg="lightgray", font=("Helvetica", 12))
        start_label.grid(row=0, column=0, padx=5, pady=5)
        self.start_entry = tk.Entry(input_frame, font=("Helvetica", 12), state=tk.DISABLED)
        self.start_entry.grid(row=0, column=1, padx=5, pady=5)

        end_label = tk.Label(input_frame, text="End Node:", bg="lightgray", font=("Helvetica", 12))
        end_label.grid(row=1, column=0, padx=5, pady=5)
        self.end_entry = tk.Entry(input_frame, font=("Helvetica", 12), state=tk.DISABLED)
        self.end_entry.grid(row=1, column=1, padx=5, pady=5)

        # Creating a button to find the shortest path.
        find_button = tk.Button(self.window, text="Find Shortest Path", command=self.find_shortest_path,
                                bg="green", fg="white", font=("Helvetica", 12, "bold"))
        find_button.pack(pady=10)

        # Creating a label to display the result.
        self.result_label = tk.Label(self.window, text="", bg="lightgray", font=("Helvetica", 12, "bold"))
        self.result_label.pack()

    def node_clicked(self, node_name):
        """
        Handle the click event when a node is clicked.
        """
        print(f"Node {node_name} clicked!")

        # Set the selected node as the starting or ending point in the Graph class
        if self.graph.selected_start_node is None:
            self.graph.selected_start_node = node_name
            entry = self.start_entry
        elif self.graph.selected_end_node is None and node_name != self.graph.selected_start_node:
            self.graph.selected_end_node = node_name
            entry = self.end_entry
        else:
            # Ignore clicks after both start and end nodes are selected
            return

        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
        entry.insert(0, node_name)
        entry.config(state=tk.DISABLED)
    def find_shortest_path(self):
        start_node = self.start_entry.get()
        end_node = self.end_entry.get()

        # Input validation
        if not start_node or not end_node:
            self.result_label.config(text="Invalid input. Please enter valid node values.", fg="red")
            return

        shortest_path = self.graph.dijkstra(start_node, end_node)

        # Display node names instead of numbers in the path
        path_names = [self.graph.index_to_node_name(node) for node in shortest_path]

        self.result_label.config(text="Shortest Path: " + " -> ".join(path_names), fg="blue")

        # Reset start and end nodes after finding the shortest path
        self.reset_start_end_nodes()

        # Animate the path
        self.animate_path(shortest_path)

    def animate_path(self, path):
        """
        Animate the traversal of the shortest path on the graph.
        """
        if not path:
            return

        # Recursive function for animation.
        def animate(index):
            if index < len(path) - 1:
                (x1, y1), (x2, y2) = self.node_coordinates[self.graph.index_to_node_name(path[index])], \
                    self.node_coordinates[self.graph.index_to_node_name(path[index + 1])]
                line_tag = f"{self.graph.index_to_node_name(path[index])}_{self.graph.index_to_node_name(path[index + 1])}"
                self.canvas.create_line(x1, y1, x2, y2, width=2, fill="red", tags=line_tag)
                self.window.after(1000, animate, index + 1)  # 1000 milliseconds (1 second) delay
            else:
                # Reset the canvas after animation is complete.
                self.canvas.delete("red_lines")  # Tag for red lines

        # Start the animation with the first edge.
        animate(0)

    def reset_start_end_nodes(self):
        """
        Reset start and end nodes after finding the shortest path.
        """
        self.graph.selected_start_node = None
        self.graph.selected_end_node = None
        self.start_entry.config(state=tk.NORMAL)
        self.start_entry.delete(0, tk.END)
        self.end_entry.config(state=tk.NORMAL)
        self.end_entry.delete(0, tk.END)

# ... Rest of the code remains the same ...

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
                    x1, y1 = self.graph.vertex_coordinates[i]
                    x2, y2 = self.graph.vertex_coordinates[j]
                    self.canvas.create_line(x1, y1, x2, y2, width=2, fill="black")

        # Drawing the vertices on the map.
        for i in range(self.graph.vertices):
            x, y = self.graph.vertex_coordinates[i]
            node_name = self.graph.index_to_node_name(i)
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white", outline="black", tags=node_name)
            self.canvas.create_text(x, y, text=node_name, fill="black", tags=node_name)

            # Bind click event to each node
            self.canvas.tag_bind(node_name, '<Button-1>', lambda event, name=node_name: self.node_clicked(name))

        # Display the result label again after the canvas is reset.
        self.result_label.config(text="", fg="black")
