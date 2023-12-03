import os

def part_one(lines:list[str]) -> int:
    coords = set()
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for dy in range(y - 1, y + 2):
                for dx in range(x - 1, x + 2):
                    if dy < 0 or dy >= len(lines) or dx < 0 or dx >= len(lines[dy]) or not lines[dy][dx].isdigit():
                        continue
                    while dx > 0 and lines[dy][dx - 1].isdigit():
                        dx -= 1
                    coords.add((dy, dx))

    numbers = []
    for y, x in coords:
        number_string = ""
        while x < len(lines[y]) and lines[y][x].isdigit():
            number_string += lines[y][x]
            x += 1
        numbers.append(int(number_string))
    return sum(numbers)


def part_two(lines:list[str]) -> int:
    total_gear_ratio= 0
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch != "*":
                continue
            coordinate_pairs = set()
            for dy in range(y-1, y+2):
                for dx in range(x-1, x+2):
                    if dy < 0 or dy >= len(lines) or dx < 0 or dx >= len(lines[dy]) or not lines[dy][dx].isdigit():
                        continue
                    while dx > 0 and lines[dy][dx - 1].isdigit():
                        dx -= 1
                    coordinate_pairs.add((dy, dx))      
            if len(coordinate_pairs) != 2:
                continue
            ns = []
            for dy, dx in coordinate_pairs:
                s = ""
                while dx < len(lines[dy]) and lines[dy][dx].isdigit():
                    s += lines[dy][dx]
                    dx += 1
                ns.append(int(s))          
            gear_ratio = ns[0] * ns[1]
            total_gear_ratio += gear_ratio
    return total_gear_ratio


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    print(part_one(lines))
    print(part_two(lines))
