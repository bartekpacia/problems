graph: dict[str, set[str]] = {}

with open("sample1.txt") as file:
    for line in file:
        node1, node2 = line.strip().split("-")
        if node1 not in graph:
            graph[node1] = set([node1])
        else:
            graph[node1].add(node2)

        if node2 not in graph:
            graph[node2] = set([node1])
        else:
            graph[node2].add(node1)

already_visited: set[str] = set()
already_visited_lowercase: set[str] = set()


def visit(node: str, path: list[str]):
    new_path = path.copy()
    new_path.append(node)
    if node == "end":
        print(f"end reached: {new_path}")
        return

    if node.lower() == node:
        if node in already_visited:
            already_visited_lowercase.add(node)

    already_visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in already_visited:
            visit(neighbor, new_path)


for node in graph["start"]:
    visit(node, [])
