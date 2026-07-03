from terrain_navigation.terrain import (
    generate_flat_terrain,
    generate_mountain_barrier,
    generate_random_terrain,
)


SCENARIOS = {
    "flat_terrain": generate_flat_terrain,
    "mountain_barrier": generate_mountain_barrier,
    "random_terrain": generate_random_terrain,
}


def get_scenario(name):
    if name not in SCENARIOS:
        available = ", ".join(SCENARIOS.keys())
        raise ValueError(
            f"Unknown scenario '{name}'. Available scenarios: {available}"
        )

    return SCENARIOS[name]()