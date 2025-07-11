from itertools import cycle
import sys
import math


def read_input(filename):
    with open(filename) as f:
        instructions = f.readline().strip()
        next(f)
        map_nodes = dict()
        for line in f:
            line = line.strip()
            if not line:
                continue
            items = line.split(" = ")
            node = items[0]
            paths = items[1].strip("()")
            left, right = paths.split(", ")
            map_nodes[node] = (left, right)
        return instructions, map_nodes


def steps_to_cross_map(instructions, map_nodes):
    return _steps_to_cross_map(instructions, map_nodes, "AAA", {"ZZZ"})


def steps_to_cross_the_map_for_ghosts(instructions, map_nodes):
    end_nodes = {n for n in map_nodes if n.endswith("Z")}
    start_nodes = {n for n in map_nodes if n.endswith("A")}
    ghost_steps = [
        _steps_to_cross_map(instructions, map_nodes, start_node, end_nodes)
        for start_node in start_nodes
    ]
    return math.lcm(*ghost_steps)


def _steps_to_cross_map(instructions, map_nodes, start_node, end_nodes):
    assert end_nodes
    assert start_node in map_nodes
    assert all(node in map_nodes for node in end_nodes)
    steps = 0
    node = start_node
    for instruction in cycle(instructions):
        if node in end_nodes:
            break
        lr_idx = 0 if instruction == "L" else 1
        node = map_nodes[node][lr_idx]
        steps += 1
    return steps


def main():
    assert len(sys.argv) == 2, "missing arg: <input_file>"
    instructions, map_nodes = read_input(sys.argv[1])
    n_steps = steps_to_cross_map(instructions, map_nodes)
    print(f"Steps needed to cross the Haunted Wasteland: {n_steps}")
    n_steps = steps_to_cross_the_map_for_ghosts(instructions, map_nodes)
    print(f"Steps needed to cross the Haunted Wasteland for ghosts: {n_steps}")


if __name__ == "__main__":
    main()
