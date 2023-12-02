import os

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def part_one(lines:list[str]) -> int: 
    sum_of_ids = 0
    for line in lines:
        split = line.split(": ")
        game_number = int(split[0].replace("Game ", ""))
        rounds = split[1].split(";")
        for round in rounds: 
            cubes = round.split(", ")
            for cube in cubes:
                cube_split = cube.strip().split(" ")
                color = cube_split[1]
                count = int(cube_split[0])
                match color:
                    case "red":
                        if count > MAX_RED:
                            break
                    case "blue":
                        if count > MAX_BLUE:
                            break
                    case "green":
                        if count > MAX_GREEN:
                            break
            else:
                continue
            break
        else:
            sum_of_ids += game_number
    return sum_of_ids

def part_two(lines:list[str]) -> int:
    sum_of_powers = 0
    for line in lines:
        split = line.split(": ")
        rounds = split[1].split(";")

        max_red = 0
        max_green = 0
        max_blue = 0

        for round in rounds: 
            cubes = round.split(", ")
            for cube in cubes:
                cube_split = cube.strip().split(" ")
                color = cube_split[1]
                count = int(cube_split[0])
                match color:
                    case "red":
                        if count > max_red:
                            max_red = count
                    case "blue":
                        if count > max_blue:
                            max_blue = count
                    case "green":
                        if count > max_green:
                            max_green = count
          
        sum_of_powers += (max_blue * max_green * max_red)
    return sum_of_powers

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    print(part_one(lines))
    print(part_two(lines))