from mygraph import Graph
from a_star import a_star
from utils import create_sample_graph

def main()
    graph = Graph()
    create_sample_graph(graph)

    start = input("Enter start location: ").strip()
    goal = input("Enter destination: ").strip()

    path, cost = a_star(graph, start, goal)

    if path:
        print("\n✅ Shortest Path Found:")
        print(" -> ".join(path))
        print(f"Total Distance: {cost}")
    else:
        print("❌ No path found")

if __name__ == "__main__":
    main()