
import os

def part_one(lines: list[str]) -> int: 
    nice_strings = 0
    for line in lines:
        vowel_count = 0
        for char in line:
            if char in 'aeiou':
                vowel_count += 1
        if vowel_count < 3:
            continue   

        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                break
        else:
            continue  

        if any(substring in line for substring in ["ab", "cd", "pq", "xy"]):
            continue
        nice_strings += 1
    return nice_strings

def part_two(lines: list[str]) -> int:
    nice_strings = 0
    for line in lines:
        first = False
        for i in range(len(line)-3):
            sub = line[i:i+2]
            if sub in line[i+2:]:
                first = True
                break
        if not first:
            continue
        second = False
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                second = True
                break
        if second:
            nice_strings += 1
    return nice_strings

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as f:
        lines = f.read().splitlines()

    print(part_one(lines))
    print(part_two(lines))
