import os
from math import prod

def part_one(lines: list[str]) -> int:
    total = 0
    for line in lines:
        measurements = [int(measurement) for measurement in line.split("x")]
        side1 = measurements[0] * measurements[1]
        side2 = measurements[1] * measurements[2]
        side3 = measurements[0] * measurements[2]

        total += (2 * side1) + (2 * side2) + (2*side3) + min(side1, side2, side3)
    return total

def part_two(lines: list[str]) -> int:
    total = 0
    for line in lines:
        measurements = [int(measurement) for measurement in line.split("x")]
        total += prod(measurements)
        measurements.remove(max(measurements))
        total += 2 * measurements[0] + 2 * measurements[1]
    return total

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as f:
        lines = f.read().splitlines()

    print(part_one(lines))
    print(part_two(lines))
