def part_one(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        for char in line:
            if char.isdigit():
                sum += int(char) * 10
                break
        for char in reversed(line):
            if char.isdigit():
                sum += int(char)
                break
    return sum


str_digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]


def part_two(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        digits = []
        for idx, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
            for d, val in enumerate(str_digits):
                if line[idx:].startswith(val):
                    digits.append(d + 1)
        sum += (digits[0] * 10) + digits[-1]
    return sum


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    print(part_one(lines))
    print(part_two(lines))
