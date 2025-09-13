import sys
import collections


def read_input(filename):
    with open(filename) as f:
        line = f.readline()
    line.strip()
    timers = line.split(",")
    return [int(x) for x in timers]


def reproduce_one_day(timer_counts):
    fish_to_reproduce = timer_counts.pop(0)  # poping will decrease the timers
    timer_counts[6] += fish_to_reproduce  # reset timer for fish that reproduced
    timer_counts.append(fish_to_reproduce)  # new fish at timer 8


def reproduce(init_state, days):
    init_counts = collections.Counter(init_state)
    timer_counts = [init_counts[t] for t in range(9)]
    # print(init_state)
    # print(timer_counts)
    for _ in range(days):
        reproduce_one_day(timer_counts)
        # print(timer_counts)
    return sum(timer_counts)


def main(args):
    if len(args) != 2:
        raise RuntimeError(
            "incorrect number of arguments, expecting: <input.txt> <number_of_days>"
        )

    init_state = read_input(args[0])
    days = int(args[1])
    n_fish = reproduce(init_state, days)
    print("Number of lanternfish after {} days: {}".format(days, n_fish))


if __name__ == "__main__":
    main(sys.argv[1:])
