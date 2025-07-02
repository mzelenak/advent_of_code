import sys


def read_input(filename):
    with open(filename) as f:
        line = f.readline()
        return line.strip().split()


def blink(stone):
    new_stones = []
    n_digits = len(stone)
    if stone == "0":
        new_stones.append("1")
    elif n_digits % 2 == 0:
        new_stones.append(stone[: n_digits // 2])
        new_stones.append(str(int(stone[n_digits // 2 :])))
    else:
        new_stones.append(str(int(stone) * 2024))
    return new_stones


def solution1(stones, n_blinks):
    print(f"n_stones (initial): {len(stones)}")
    for blink_idx in range(n_blinks):
        new_stones = []
        for stone in stones:
            new_stones.extend(blink(stone))
        stones = new_stones
        print(f"n_stones {blink_idx+1}: {len(stones)}")
    return len(stones)


def solution2(stones, n_blinks):
    memory = {}

    def n_stones(stone, n_blinks):
        if (stone, n_blinks) in memory:
            return memory[(stone, n_blinks)]
        if n_blinks == 0:
            return 1
        total = sum(n_stones(new_stone, n_blinks - 1) for new_stone in blink(stone))
        memory[(stone, n_blinks)] = total
        print(f"n_stones({stone}, {n_blinks}): {total}")
        return total

    return sum(n_stones(stone, n_blinks) for stone in stones)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if len(argv) != 2:
        print(
            "Usage: python plutonian_pebbles.py <input file> <n_blinks>",
            file=sys.stderr,
        )
        sys.exit(1)
    input_file = argv[0]
    n_blinks = int(argv[1])
    assert n_blinks >= 0, "n_blinks must be a non-negative integer"
    stones = read_input(input_file)
    assert stones, "no stones provided in the input file"
    assert all(stone.isdigit() for stone in stones), "all stones must be non-negative integers"
    # print(solution1(stones, n_blinks))
    print(solution2(stones, n_blinks))


if __name__ == "__main__":
    main()
