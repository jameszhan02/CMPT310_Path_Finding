def movement_cost(current_elevation, next_elevation):
    """
    Calculate the cost of moving from one cell to another.

    Every move has a cost of 1. If the next cell has a different
    elevation, extra cost is added. This makes steeper paths
    more expensive than flatter ones.
    """
    elevation_difference = abs(next_elevation - current_elevation)

    return 1 + elevation_difference


def build_graph(terrain, obstacles):
    """
    Build a weighted graph from the terrain grid.

    Every free cell becomes a node in the graph. Each node is
    connected to its valid neighboring cells, and the edge weight
    is based on the elevation difference between the two cells.
    Obstacle cells are skipped because they cannot be crossed.
    """
    rows, cols = terrain.shape
    graph = {}

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    for row in range(rows):
        for col in range(cols):

            if obstacles[row, col]:
                continue

            current_node = (row, col)
            graph[current_node] = []

            for dr, dc in directions:
                neighbor_row = row + dr
                neighbor_col = col + dc

                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    if not obstacles[neighbor_row, neighbor_col]:

                        cost = movement_cost(
                            terrain[row, col],
                            terrain[neighbor_row, neighbor_col],
                        )

                        graph[current_node].append(
                            ((neighbor_row, neighbor_col), cost)
                        )

    return graph