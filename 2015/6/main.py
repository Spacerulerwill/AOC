
import os

def part_one(lines: list[str]) -> int: 
    ...
    
if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as f:
        lines = f.read().splitlines()
