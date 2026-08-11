# CMPT 310 - Terrain Pathfinding

**Team: Pathfinders** (Banveet Johal, Lucas Zhang, Sheng Zhan)
CMPT 310 - D100, Introduction to Artificial Intelligence, Summer 2026

Cost-aware pathfinding on procedurally generated, elevation-weighted terrain
grids. Five classical search algorithms - **BFS, DFS, Uniform-Cost Search,
Greedy Best-First Search, and A\*** - are implemented from scratch and
compared on path cost, path length, nodes explored, and runtime across three
test scenarios (flat terrain, a mountain barrier, and random terrain).

## Repository layout

```
.
├── pathfinding.ipynb                     # Terrain/map generation + visualization exploration
├── requirements.txt                      # Python dependencies
├── cmpt310_milestone1_pathfinders/
│   └── terrain_navigation/
│       ├── terrain.py                    # Scenario generators (flat / mountain / random)
│       ├── graph.py                      # Builds a weighted grid graph from terrain + obstacles
│       ├── search.py                     # BFS, DFS, UCS, Greedy Best-First, A*
│       ├── metrics.py                    # Path cost / length / elevation-gain calculations
│       ├── scenarios.py                  # Scenario registry (get_scenario)
│       ├── visualize.py                  # Path + comparison plot generation
│       └── main.py                       # Runs all 5 algorithms on a chosen scenario
│   └── outputs/                          # Generated results.txt, paths.png, comparison.png per scenario
├── poster/
│   ├── CMPT310_Pathfinding_Poster.pdf         # Project poster
│   └── CMPT310_Pathfinding_Poster_preview.png
└── docs/
    ├── How_To_Guide.pdf                       # Submission deliverable
    └── Project_Write_Up.pdf                   # Submission deliverable
```

## Setup

Requires Python 3.9+.

```bash
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the pathfinding pipeline

From the `cmpt310_milestone1_pathfinders/` directory, run:

```bash
cd cmpt310_milestone1_pathfinders
python -m terrain_navigation.main
```

This will:

1. Build the terrain/obstacle grid for the selected scenario.
2. Construct a weighted graph (edge cost = `1 + |elevation difference|`).
3. Run BFS, DFS, UCS, Greedy Best-First Search, and A\* from `start` to `goal`.
4. Print a summary of each algorithm's path cost, nodes explored, and runtime.
5. Save results to `outputs/<scenario>_start<r>-<c>_goal<r>-<c>/`:
   - `results.txt` - text summary of every algorithm's metrics
   - `paths.png` - each algorithm's explored path drawn on the terrain
   - `comparison.png` - bar charts comparing cost, nodes explored, and runtime

### Switching scenarios

Open `cmpt310_milestone1_pathfinders/terrain_navigation/main.py` and change the
`get_scenario(...)` call:

```python
scenario = get_scenario("flat_terrain")      # baseline, no obstacles
scenario = get_scenario("mountain_barrier")   # high-cost elevation ridge
scenario = get_scenario("random_terrain")     # scattered obstacles + a smooth hill
```

## Notebook

`pathfinding.ipynb` contains an earlier, standalone exploration of terrain
generation and visualization (`generate_map` / `visualize_map`) with
side-by-side parameter comparisons. Open it with Jupyter or VS Code's
notebook viewer:

```bash
jupyter notebook pathfinding.ipynb
```

## Poster and submission documents

- `poster/CMPT310_Pathfinding_Poster.pdf` - the project poster.
- `docs/How_To_Guide.pdf` and `docs/Project_Write_Up.pdf` - the course
  submission deliverables.
