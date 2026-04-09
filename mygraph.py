class Graph:
    def __init__(self):
        self.edges = {}
        self.heuristics = {}

    def add_edge(self, from_node, to_node, distance):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, distance))

    def set_heuristic(self, node, value):
        self.heuristics[node] = value

    def get_neighbors(self, node):
        return self.edges.get(node, [])