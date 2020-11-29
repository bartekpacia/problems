line = input().split(" ")
n = int(line[0])  # nodes
m = int(line[1])  # edges
graph = {}


def find_lowest_cost_node(costs, processed):
    lowest_cost_node = None
    lowest_cost = float("inf")
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
            lowest_cost = cost

    return lowest_cost_node, lowest_cost


def shortest_path(start, end):
    costs = {}
    costs[start] = 0
    processed = []

    node, cost = find_lowest_cost_node(costs, processed)
    while node is not None:
        neighbors = graph[node]
        for neighbor, neighbor_cost in neighbors.items():
            new_cost = neighbor_cost + cost
            if costs.get(neighbor) is None or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost

        processed.append(node)
        node, cost = find_lowest_cost_node(costs, processed)

    if costs.get(end) is None:
        return -1
    else:
        return costs[end]


for i in range(m):
    line = input().split(" ")
    a = int(line[0])
    b = int(line[1])
    w = int(line[2])

    if graph.get(a) is None:
        graph[a] = {}

    if graph.get(a).get(b) is not None:
        if graph[a][b] > w:
            graph[a][b] = w
    elif graph.get(a).get(b) is None:
        graph[a][b] = w

    if graph.get(b) is None:
        graph[b] = {}

    if graph.get(b).get(a) is not None:
        if graph[b][a] > w:
            graph[b][a] = w
    elif graph.get(b).get(a) is None:
        graph[b][a] = w


distance = shortest_path(1, n)
print(distance)
