import heapq
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


def manhattan_distance(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


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

def ucs(graph, start, goal):
    frontier = [(0, start)]
    best_cost = {start: 0}
    parent = {start: None}
    visited = set()
    nodes_explored = 0
 
    while frontier:
        current_cost, current = heapq.heappop(frontier) 
        if current in visited:
            continue
 
        visited.add(current)
        nodes_explored += 1
 
        if current == goal:
            break
 
        for neighbor, cost in graph[current]:
            new_cost = current_cost + cost
 
            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(frontier, (new_cost, neighbor))
 
    path = reconstruct_path(parent, start, goal)
 
    return {
        "algorithm": "UCS",
        "path": path,
        "nodes_explored": nodes_explored,
    }

def greedy(graph, start, goal):
    frontier = [(manhattan_distance(start, goal), start)]
    visited = set()
    parent = {start: None}
    nodes_explored = 0
 
    while frontier:
        heuristic, current = heapq.heappop(frontier)
 
        if current in visited:
            continue
 
        visited.add(current)
        nodes_explored += 1
 
        if current == goal:
            break
 
        for neighbor, cost in graph[current]:
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = current
                heapq.heappush(
                    frontier,
                    (manhattan_distance(neighbor, goal), neighbor),
                )
 
    path = reconstruct_path(parent, start, goal)
 
    return {
        "algorithm": "Greedy",
        "path": path,
        "nodes_explored": nodes_explored,
    }

def astar(graph, start, goal):
    start_f = manhattan_distance(start, goal)
    frontier = [(start_f, 0, start)]
    best_cost = {start: 0}
    parent = {start: None}
    visited = set()
    nodes_explored = 0
 
    while frontier:
        f_value, current_cost, current = heapq.heappop(frontier)
 
        if current in visited:
            continue
 
        visited.add(current)
        nodes_explored += 1
 
        if current == goal:
            break
 
        for neighbor, cost in graph[current]:
            new_cost = current_cost + cost
 
            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                parent[neighbor] = current
                f_new = new_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(frontier, (f_new, new_cost, neighbor))
 
    path = reconstruct_path(parent, start, goal)
 
    return {
        "algorithm": "A*",
        "path": path,
        "nodes_explored": nodes_explored,
    }

