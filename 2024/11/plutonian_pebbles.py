import sys


def read_input(filename):
    with open(filename) as f:
        line = f.readline()
        return line.strip().split()
        

def blink(stones):
    new_stones = []
    for stone in stones:
        n_digits = len(stone)
        if stone == "0":
            new_stones.append("1")
        elif n_digits % 2 == 0:
            new_stones.append(stone[:n_digits // 2])
            new_stones.append(str(int(stone[n_digits // 2:])))
        else:
            new_stones.append(str(int(stone) * 2024))

    return new_stones


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if len(argv) != 2:
        raise RuntimeError("missing arg: <input file> <n_blinks>")
    input_file = argv[0]
    n_blinks = int(argv[1])
    stones = read_input(input_file)

    print("blinks\t#stones:")
    print("0:\t{}".format(len(stones)))
    for blink_idx in range(n_blinks):
        stones = blink(stones)
        print("{}:\t{}".format(blink_idx+1, len(stones)))
    
    return len(stones)

if __name__ == "__main__":
    print(main())