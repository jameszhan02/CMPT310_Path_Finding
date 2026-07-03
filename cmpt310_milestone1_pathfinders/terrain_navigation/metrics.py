def calculate_path_metrics(path, terrain, graph):
    """
    Calculate statistics for the path returned by a search algorithm.
    BFS and DFS do not use weighted cost during search, but we still calculate the weighted cost afterward for comparison.
    """
    if not path:
        return {
            "path_found": False,
            "path_length": 0,
            "weighted_path_cost": 0,
            "elevation_gain": 0,
        }

    total_cost = 0
    elevation_gain = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        current_elevation = terrain[current]
        next_elevation = terrain[next_node]

        if next_elevation > current_elevation:
            elevation_gain += next_elevation - current_elevation

        for neighbor, cost in graph[current]:
            if neighbor == next_node:
                total_cost += cost
                break

    return {
        "path_found": True,
        "path_length": len(path) - 1,
        "weighted_path_cost": round(total_cost, 2),
        "elevation_gain": round(elevation_gain, 2),
    }