"""Water Jug Problem using Breadth First Search (BFS).
Run with: python water_jug.py
"""
from collections import deque


def get_next_states(state, cap_x, cap_y):
    """Return every (new_state, action) reachable from `state` in one move."""
    x, y = state
    moves = [
        ((cap_x, y), "Fill Jug X completely"),
        ((x, cap_y), "Fill Jug Y completely"),
        ((0, y), "Empty Jug X"),
        ((x, 0), "Empty Jug Y"),
    ]
    # Pour X -> Y
    pour = min(x, cap_y - y)
    moves.append(((x - pour, y + pour), "Pour water from Jug X to Jug Y"))
    # Pour Y -> X
    pour = min(y, cap_x - x)
    moves.append(((x + pour, y - pour), "Pour water from Jug Y to Jug X"))
    return moves


def water_jug_bfs(cap_x, cap_y, target):
    """Find the shortest sequence of moves that leaves `target` litres in a jug."""
    start = (0, 0)
    queue = deque([start])
    parent = {start: (None, "Start with both jugs empty")}  # state -> (previous, action)
    visited = {start}

    while queue:
        state = queue.popleft()
        if state[0] == target or state[1] == target:
            # Walk back through the parents to build the path
            path = []
            while state is not None:
                prev, action = parent[state]
                path.append((state, action))
                state = prev
            return path[::-1], len(visited)

        for nxt, action in get_next_states(state, cap_x, cap_y):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = (state, action)
                queue.append(nxt)

    return None, len(visited)


def main():
    cap_x = int(input("Enter capacity of Jug X (litres): "))
    cap_y = int(input("Enter capacity of Jug Y (litres): "))
    target = int(input("Enter target amount (litres): "))

    path, explored = water_jug_bfs(cap_x, cap_y, target)

    if path is None:
        print("\nNo solution exists for the given capacities and target.")
        return

    print(f"\nSolution found in {len(path) - 1} steps (states explored: {explored})\n")
    print(f"{'Step':<6}{'(X, Y)':<10}Action")
    print("-" * 50)
    for step, (state, action) in enumerate(path):
        print(f"{step:<6}{str(state):<10}{action}")
    print(f"\nTarget of {target} litres measured successfully!")


if __name__ == "__main__":
    main()
