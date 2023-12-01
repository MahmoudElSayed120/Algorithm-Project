# graph.py
import random
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    """
    Class to represent a graph and perform Dijkstra's algorithm to find the shortest path.

    Attributes:
    - vertices: int
        The number of vertices in the graph.
    - adjacency_matrix: list of lists
        The adjacency matrix representing the graph.
    """

    def __init__(self, vertices):
        """
        Constructor to instantiate the Graph class.

        Parameters:
        - vertices: int
            The number of vertices in the graph.

        Raises:
        - ValueError:
            Throws an error if the number of vertices is less than 2.
        """

        # Verifying that the number of vertices is valid.
        if vertices < 2:
            raise ValueError("Number of vertices should be at least 2.")

        # Assigning the number of vertices to the instance variable.
        self.vertices = vertices

        # Creating an empty adjacency matrix.
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        """
        Adds an edge to the graph.

        Parameters:
        - source: int
            The source vertex of the edge.
        - destination: int
            The destination vertex of the edge.
        - weight: int
            The weight of the edge.

        Raises:
        - ValueError:
            Throws an error if the source or destination vertex is invalid.
        """

        # Verifying that the source and destination vertices are valid.
        if source < 0 or source >= self.vertices or destination < 0 or destination >= self.vertices:
            raise ValueError("Invalid source or destination vertex.")

        # Adding the edge to the adjacency matrix.
        self.adjacency_matrix[source][destination] = weight
        self.adjacency_matrix[destination][source] = weight

    def dijkstra(self, start_vertex, end_vertex):
        """
        Performs Dijkstra's algorithm to find the shortest path between two vertices.

        Parameters:
        - start_vertex: int
            The starting vertex for the shortest path.
        - end_vertex: int
            The ending vertex for the shortest path.

        Returns:
        - list of int:
            The shortest path from the start_vertex to the end_vertex.
        """

        # Creating a list to store the shortest distances from the start_vertex to all other vertices.
        distances = [float('inf')] * self.vertices
        distances[start_vertex] = 0

        # Creating a list to store the visited status of each vertex.
        visited = [False] * self.vertices

        # Creating a list to store the previous vertex in the shortest path.
        previous = [-1] * self.vertices

        # Looping through all the vertices to find the shortest path.
        for _ in range(self.vertices):
            # Finding the vertex with the minimum distance from the start_vertex.
            min_distance = float('inf')
            min_vertex = -1
            for v in range(self.vertices):
                if not visited[v] and distances[v] < min_distance:
                    min_distance = distances[v]
                    min_vertex = v

            # Marking the minimum distance vertex as visited.
            visited[min_vertex] = True

            # Updating the distances of the neighboring vertices.
            for v in range(self.vertices):
                if not visited[v] and self.adjacency_matrix[min_vertex][v] != 0:
                    new_distance = distances[min_vertex] + self.adjacency_matrix[min_vertex][v]
                    if new_distance < distances[v]:
                        distances[v] = new_distance
                        previous[v] = min_vertex

        # Backtracking from the end_vertex to construct the shortest path.
        path = []
        current_vertex = end_vertex
        while current_vertex != -1:
            path.append(current_vertex)
            current_vertex = previous[current_vertex]

        # Reversing the path to get the correct order.
        path.reverse()

        return path

    def create_random_graph(self):
        """
        Creates a random graph with the given number of vertices.

        Returns:
        - Graph:
            The randomly generated graph.
        """
        random_graph = Graph(self.vertices)

        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                # Randomly decide whether to add an edge between vertices i and j.
                if random.choice([True, False]):
                    weight = random.randint(1, 10)
                    random_graph.add_edge(i, j, weight)

        return random_graph

    def visualize_graph(self):
        """
        Visualizes the graph using networkx and matplotlib.
        """
        G = nx.Graph()

        for i in range(self.vertices):
            G.add_node(i)

        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                if self.adjacency_matrix[i][j] != 0:
                    G.add_edge(i, j, weight=self.adjacency_matrix[i][j])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
