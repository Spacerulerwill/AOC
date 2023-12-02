import os

def part_one(input_string: str) -> int:
    floor = 0
    for char in input_string:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor

def part_two(input_string:str) -> int:
    floor = 0
    position = 0
    while floor != -1:
        char = input_string[position]
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        position += 1
    return position

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as f:
        input_string = f.read()

    print(part_one(input_string))
    print(part_two(input_string))