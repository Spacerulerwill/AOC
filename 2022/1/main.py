import os


def part_one(input_string: str) -> int:
    groupedCalories = input_string.split("\n\n")
    highest = 0
    for group in groupedCalories:
        total = sum(int(calorie) for calorie in group.split("\n"))
        if total > highest:
            highest = total
    return highest


def part_two(input_string: str) -> int:
    groupedCalories = input_string.split("\n\n")
    elvesCalories = []
    for group in groupedCalories:
        elvesCalories.append(sum(
            int(calorie) for calorie in group.split("\n")))
    return sum(sorted(elvesCalories)[-3:])


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt", "r") as f:
        input_string = f.read()

    print(part_one(input_string))
    print(part_two(input_string))
