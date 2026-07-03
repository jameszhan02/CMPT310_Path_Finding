import numpy as np

def generate_flat_terrain(rows=25, cols=25):
    """
    Create a simple flat terrain with no obstacles.
    Every cell has the same elevation, so this is used as the baseline map for testing the
    search algorithms.
    """
    terrain = np.ones((rows, cols))

    obstacles = np.zeros((rows, cols), dtype=bool)

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    return {
        "name": "flat_terrain",
        "description": "Flat terrain with no obstacles. Used as a simple baseline.",
        "terrain": terrain,
        "obstacles": obstacles,
        "start": start,
        "goal": goal,
    }

def generate_mountain_barrier(rows=25, cols=25):
    """
    Create a terrain with a mountain running across the map.
    The mountain has a much higher elevation than the rest of the map, making it more expensive 
    to travel through.
    """

    terrain = np.ones((rows, cols))

    center_row = rows // 2

    for row in range(rows):
        distance_from_center = abs(row - center_row)

        if distance_from_center <= 5:
            height = 12 - distance_from_center * 2
            terrain[row, :] += height

    rng = np.random.default_rng(4)
    terrain += rng.normal(0, 0.3, size=(rows, cols))
    terrain = np.maximum(0, terrain).round(2)

    obstacles = np.zeros((rows, cols), dtype=bool)

    start = (4, 0)
    goal = (20, 24)

    return {
        "name": "mountain_barrier",
        "description": "A high mountain ridge creates costly elevation changes.",
        "terrain": terrain,
        "obstacles": obstacles,
        "start": start,
        "goal": goal,
    }


def generate_random_terrain(rows=25, cols=25, seed=42):
    """
    Create a random terrain with different elevations and obstacles.
    This map is used to test the algorithms on a more realistic environment where the terrain 
    changes across the map.
    """
    rng = np.random.default_rng(seed)

    terrain = rng.normal(3, 1.5, size=(rows, cols))
    terrain = np.maximum(0, terrain)

    # Add one smooth hill
    x = np.linspace(-1, 1, cols)
    y = np.linspace(-1, 1, rows)
    xx, yy = np.meshgrid(x, y)

    hill = 8 * np.exp(-((xx - 0.2) ** 2 + (yy + 0.1) ** 2) * 5)
    terrain += hill
    terrain = terrain.round(2)

    obstacles = rng.random((rows, cols)) < 0.12

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    obstacles[start] = False
    obstacles[goal] = False

    return {
        "name": f"random_terrain",
        "description": "Random elevation map with scattered obstacles.",
        "terrain": terrain,
        "obstacles": obstacles,
        "start": start,
        "goal": goal,
    }