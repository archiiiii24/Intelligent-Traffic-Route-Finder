import heapq

def a_star(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current), g_cost[current]

        for neighbor, cost in graph.get_neighbors(current):
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                priority = new_cost + graph.heuristics.get(neighbor, 0)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return None, float('inf')


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path