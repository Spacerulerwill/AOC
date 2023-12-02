import os

def part_one(input_string:str) -> int:
    visited_houses = set()
    visited_houses.add((0,0))
    x, y = (0,0)
    for char in input_string:
        match char:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
        visited_houses.add((x,y))
    return len(visited_houses)

def part_two(input_string:str) -> int:
    visited_houses = set()
    visited_houses.add((0,0))
    santa_x, santa_y = (0,0)
    robot_santa_x, robot_santa_y = (0,0)
    for i in range(0,len(input_string),2):
        match input_string[i]:
            case "^":
                santa_y += 1
            case "v":
                santa_y -= 1
            case ">":
                santa_x += 1
            case "<":
                santa_x -= 1
        visited_houses.add((santa_x,santa_y))
        match input_string[i+1]:
            case "^":
                robot_santa_y += 1
            case "v":
                robot_santa_y -= 1
            case ">":
                robot_santa_x += 1
            case "<":
                robot_santa_x -= 1
        visited_houses.add((robot_santa_x,robot_santa_y))
    return len(visited_houses)

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as f:
        input_string = f.read()

    print(part_one(input_string))
    print(part_two(input_string))
