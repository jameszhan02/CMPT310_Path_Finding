import os
 
import numpy as np
import matplotlib
 
matplotlib.use("Agg")
 
import matplotlib.pyplot as plt
 
 
def draw_terrain(ax, terrain, obstacles, start, goal):

    display = np.ma.masked_where(obstacles, terrain)
 
    image = ax.imshow(display, cmap="terrain", origin="upper")
 
    # Draw obstacles as solid black cells on top of the terrain.
    obstacle_overlay = np.zeros((*obstacles.shape, 4))
    obstacle_overlay[obstacles] = [0, 0, 0, 1]
    ax.imshow(obstacle_overlay, origin="upper")
 
    ax.plot(start[1], start[0], marker="o", color="blue",
            markersize=9, markeredgecolor="white", label="Start")
    ax.plot(goal[1], goal[0], marker="*", color="red",
            markersize=15, markeredgecolor="white", label="Goal")
 
    ax.set_xticks([])
    ax.set_yticks([])
 
    return image
 
 
def plot_all_paths(scenario, results, save_path=None):
    
    terrain = scenario["terrain"]
    obstacles = scenario["obstacles"]
    start = scenario["start"]
    goal = scenario["goal"]
 
    figure, axes = plt.subplots(
        1, len(results),
        figsize=(4.2 * len(results), 5.2),
        facecolor="white",
    )
 
    if len(results) == 1:
        axes = [axes]
 
    for ax, result in zip(axes, results):
        draw_terrain(ax, terrain, obstacles, start, goal)
 
        path = result["path"]
 
        if path:
            rows = [node[0] for node in path]
            cols = [node[1] for node in path]
            ax.plot(cols, rows, color="crimson", linewidth=2.5)
 
        ax.set_title(
            f"{result['algorithm']}\n"
            f"cost = {result['weighted_path_cost']}, "
            f"explored = {result['nodes_explored']}",
            fontsize=13,
        )
 
    figure.suptitle(
        f"Scenario: {scenario['name']} "
        f"(start {start}, goal {goal})",
        fontsize=16,
    )
 
    figure.tight_layout()
 
    if save_path:
        figure.savefig(save_path, dpi=150, facecolor="white",
                       bbox_inches="tight")
        plt.close(figure)
    else:
        plt.show()
 
 
def plot_comparison(scenario, results, save_path=None):

    names = [result["algorithm"] for result in results]
 
    metrics = [
        ("Weighted path cost", [r["weighted_path_cost"] for r in results]),
        ("Nodes explored", [r["nodes_explored"] for r in results]),
        ("Runtime (seconds)", [r["runtime_seconds"] for r in results]),
    ]
 
    figure, axes = plt.subplots(1, 3, figsize=(15, 4.5), facecolor="white")
 
    colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3"]
 
    for ax, (title, values) in zip(axes, metrics):
        bars = ax.bar(names, values, color=colors[:len(names)])
        ax.set_title(title, fontsize=13)
        ax.bar_label(bars, fmt="%.4g", fontsize=10, padding=2)
        ax.margins(y=0.15)
 
    figure.suptitle(
        f"Algorithm comparison: {scenario['name']}",
        fontsize=15,
    )
 
    figure.tight_layout()
 
    if save_path:
        figure.savefig(save_path, dpi=150, facecolor="white",
                       bbox_inches="tight")
        plt.close(figure)
    else:
        plt.show()