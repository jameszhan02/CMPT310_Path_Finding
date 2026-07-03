from collections import deque


def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return []

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    path = reconstruct_path(parent, start, goal)

    return {
        "algorithm": "BFS",
        "path": path,
        "nodes_explored": nodes_explored,
    }


def dfs(graph, start, goal):
    stack = [start]
    visited = {start}
    parent = {start: None}
    nodes_explored = 0

    while stack:
        current = stack.pop()
        nodes_explored += 1

        if current == goal:
            break

        for neighbor, cost in reversed(graph[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    path = reconstruct_path(parent, start, goal)

    return {
        "algorithm": "DFS",
        "path": path,
        "nodes_explored": nodes_explored,
    }