import os
import time

from terrain_navigation.scenarios import get_scenario
from terrain_navigation.graph import build_graph
from terrain_navigation.search import bfs, dfs
from terrain_navigation.metrics import calculate_path_metrics


def run_algorithm(algorithm_function, graph, terrain, start, goal):
    start_time = time.perf_counter()

    result = algorithm_function(graph, start, goal)

    end_time = time.perf_counter()

    metrics = calculate_path_metrics(result["path"], terrain, graph)

    result.update(metrics)
    result["runtime_seconds"] = round(end_time - start_time, 6)

    return result


def print_results(result):
    print(f"\n{result['algorithm']} Results")
    print("-" * 30)
    print(f"Path found: {result['path_found']}")
    print(f"Path length: {result['path_length']}")
    print(f"Nodes explored: {result['nodes_explored']}")
    print(f"Runtime: {result['runtime_seconds']} seconds")
    print(f"Weighted path cost: {result['weighted_path_cost']}")
    print(f"Elevation gain: {result['elevation_gain']}")


def save_results(output_dir, scenario, results):
    results_file = os.path.join(output_dir, "results.txt")

    with open(results_file, "w") as file:
        file.write(f"Scenario: {scenario['name']}\n")
        file.write(f"Description: {scenario['description']}\n")
        file.write(f"Start: {scenario['start']}\n")
        file.write(f"Goal: {scenario['goal']}\n\n")

        for result in results:
            file.write(f"{result['algorithm']} Results\n")
            file.write("-" * 30 + "\n")
            file.write(f"Path found: {result['path_found']}\n")
            file.write(f"Path length: {result['path_length']}\n")
            file.write(f"Nodes explored: {result['nodes_explored']}\n")
            file.write(f"Runtime: {result['runtime_seconds']} seconds\n")
            file.write(f"Weighted path cost: {result['weighted_path_cost']}\n")
            file.write(f"Elevation gain: {result['elevation_gain']}\n\n")


def main():
    # To test another map later, change to:
    #scenario = get_scenario("flat_terrain")
    #scenario = get_scenario("mountain_barrier")
    scenario = get_scenario("random_terrain")

    terrain = scenario["terrain"]
    obstacles = scenario["obstacles"]
    start = scenario["start"]
    goal = scenario["goal"]

    output_dir = os.path.join(
        "outputs",
        f"{scenario['name']}_start{start[0]}-{start[1]}_goal{goal[0]}-{goal[1]}",
    )

    os.makedirs(output_dir, exist_ok=True)

    graph = build_graph(terrain, obstacles)

    print("Terrain Navigation Milestone 1")
    print("=" * 40)
    print(f"Scenario: {scenario['name']}")
    print(f"Description: {scenario['description']}")
    print(f"Grid size: {terrain.shape}")
    print(f"Graph nodes: {len(graph)}")
    print(f"Start: {start}")
    print(f"Goal: {goal}")

    bfs_result = run_algorithm(bfs, graph, terrain, start, goal)
    dfs_result = run_algorithm(dfs, graph, terrain, start, goal)

    print_results(bfs_result)
    print_results(dfs_result)



    save_results(output_dir, scenario, [bfs_result, dfs_result])

    print("\nSaved outputs to:")
    print(output_dir)


if __name__ == "__main__":
    main()