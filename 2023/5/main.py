import os
import re

digits = re.compile("([0-9]+)")


def part_one(lines: list[str]) -> int:
    times = [int(num) for num in re.findall(digits, lines[0])]
    record_distances = [int(num) for num in re.findall(digits, lines[1])]
    num_races = len(times)

    total = 1
    for race_index in range(num_races):
        race_time = times[race_index]
        race_record = record_distances[race_index]
        winning_combinations = 0
        for i in range(race_time + 1):
            distance_travelled = i * (race_time - i)
            if distance_travelled > race_record:
                winning_combinations += 1
        total *= winning_combinations
    return total


def part_two(lines: list[str]) -> int:
    time = int(''.join(num for num in re.findall(digits, lines[0])))
    record_distance = int(''.join(num for num in re.findall(digits, lines[1])))

    # iterate from start to find first value of i that wins a race
    first = 0
    for i in range(time + 1):
        distance_travelled = i * (time - i)
        if distance_travelled > record_distance:
            first = i
            break

    # iterate from the end to find the last value of i that wins a race
    last = 0
    for i in range(time + 1, -1, -1):
        distance_travelled = i * (time - i)
        if distance_travelled > record_distance:
            last = i
            break
    return last - first + 1


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    print(part_one(lines))
    print(part_two(lines))
