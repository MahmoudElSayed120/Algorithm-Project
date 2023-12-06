
class Graph:
    """
    Class to represent a graph and perform Dijkstra's algorithm to find the shortest path.

    Attributes:
    - vertices: int
        The number of vertices in the graph.
    - adjacency_matrix: list of lists
        The adjacency matrix representing the graph.
    - vertex_names: dict
        A mapping from vertex index to node name.
    - selected_start_node: str or None
        The currently selected start node.
    - selected_end_node: str or None
        The currently selected end node.
    """

    def __init__(self, vertices, node_names):
        """
        Constructor to instantiate the Graph class.

        Parameters:
        - vertices: int
            The number of vertices in the graph.
        - node_names: list of str
            The names of the nodes.
        """
        # Verifying that the number of vertices is valid.
        if vertices < 2:
            raise ValueError("Number of vertices should be at least 2.")

        self.vertices = vertices
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]
        self.vertex_names = {i: name for i, name in enumerate(node_names)}

        # Manually add edges with weights based on the given information
        self.add_edge("Beirut", "Tripoli", 4)
        self.add_edge("Beirut", "Sidon", 2)
        self.add_edge("Beirut", "Anout", 2)
        self.add_edge("Beirut", "Barja", 1)
        self.add_edge("Beirut", "Hemmana", 2)
        self.add_edge("Beirut", "Zahla", 3.5)
        self.add_edge("Beirut", "Aley", 1.5)
        self.add_edge("Beirut", "Baabda", 1)

        self.add_edge("Tripoli", "Akkar", 1)
        self.add_edge("Tripoli", "Jezzine", 7)
        self.add_edge("Tripoli", "Zahla", 4)
        self.add_edge("Tripoli", "Rashaya", 7)

        self.add_edge("Anout", "Barja", 2)
        self.add_edge("Anout", "Sidon", 2.5)
        self.add_edge("Anout", "Bet ed Dine", 1)
        self.add_edge("Anout", "Aley", 3)
        self.add_edge("Anout", "Rashaya", 2)

        self.add_edge("Baabda", "Anout", 2)
        self.add_edge("Baabda", "Sidon", 2.5)
        self.add_edge("Baabda", "Aley", 1)
        self.add_edge("Baabda", "Hemmana", 1)
        self.add_edge("Baabda", "Bet ed Dine", 2)

        self.add_edge("Rashaya", "Tripoli", 7)
        self.add_edge("Rashaya", "Jezzine", 2)
        self.add_edge("Rashaya", "Zahla", 3)
        self.add_edge("Rashaya", "Anout", 1.5)

        self.add_edge("Sidon", "Naqoura", 2)
        self.add_edge("Sidon", "Beirut", 2)
        self.add_edge("Sidon", "Barja", 1)
        self.add_edge("Sidon", "Anout", 1.5)
        self.add_edge("Sidon", "Aley", 4.5)
        self.add_edge("Sidon", "Rashaya", 3)

        self.add_edge("Bet ed Dine", "Beirut", 2)
        self.add_edge("Bet ed Dine", "Aley", 2)
        self.add_edge("Bet ed Dine", "Anout", 1)

        # Initialize selected nodes to None
        self.selected_start_node = None
        self.selected_end_node = None

    def add_edge(self, source, destination, weight):
        """
        Adds an edge to the graph.

        Parameters:
        - source: str
            The source node name of the edge.
        - destination: str
            The destination node name of the edge.
        - weight: int
            The weight of the edge.

        Raises:
        - ValueError:
            Throws an error if the source or destination node name is invalid.
        """
        source_index = self.node_name_to_index(source)
        destination_index = self.node_name_to_index(destination)

        # Adding the edge to the adjacency matrix.
        self.adjacency_matrix[source_index][destination_index] = weight
        self.adjacency_matrix[destination_index][source_index] = weight

    def dijkstra(self, start_node, end_node):
        """
        Performs Dijkstra's algorithm to find the shortest path between two nodes.

        Parameters:
        - start_node: str
            The starting node for the shortest path.
        - end_node: str
            The ending node for the shortest path.

        Returns:
        - list of int:
            The shortest path from the start_node to the end_node.
        """
        start_index = self.node_name_to_index(start_node)
        end_index = self.node_name_to_index(end_node)

        distances = [float('inf')] * self.vertices
        distances[start_index] = 0
        visited = [False] * self.vertices
        previous = [-1] * self.vertices

        for _ in range(self.vertices):
            min_distance = float('inf')
            min_vertex = -1
            for v in range(self.vertices):
                if not visited[v] and distances[v] < min_distance:
                    min_distance = distances[v]
                    min_vertex = v

            visited[min_vertex] = True

            for v in range(self.vertices):
                if not visited[v] and self.adjacency_matrix[min_vertex][v] != 0:
                    new_distance = distances[min_vertex] + self.adjacency_matrix[min_vertex][v]
                    if new_distance < distances[v]:
                        distances[v] = new_distance
                        previous[v] = min_vertex

        path = []
        current_vertex = end_index
        while current_vertex != -1:
            path.append(current_vertex)
            current_vertex = previous[current_vertex]

        path.reverse()

        return path

    def node_name_to_index(self, node_name):
        """
        Converts a node name to its corresponding index.

        Parameters:
        - node_name: str
            The name of the node.

        Returns:
        - int:
            The index of the node.
        """
        for index, name in self.vertex_names.items():
            if name == node_name:
                return index
        raise ValueError(f"Node with name '{node_name}' not found.")

    def index_to_node_name(self, index):
        """
        Converts a node index to its corresponding name.

        Parameters:
        - index: int
            The index of the node.

        Returns:
        - str:
            The name of the node.
        """
        return self.vertex_names.get(index, str(index))
