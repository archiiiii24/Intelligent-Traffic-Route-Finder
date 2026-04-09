def create_sample_graph(graph):
    # Adding roads (edges)
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'E', 3)
    graph.add_edge('E', 'D', 4)
    graph.add_edge('D', 'F', 11)

    # Heuristic values (estimated distance to goal F)
    heuristics = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 3,
        'E': 4,
        'F': 0
    }

    for node, h in heuristics.items():
        graph.set_heuristic(node, h)