import os
import hashlib

def part_one(input_string: str) -> int: 
    i = 0
    while True:
        hash_hex_string = hashlib.md5((input_string + str(i)).encode()).hexdigest()
        if hash_hex_string[:5] == "00000":
            return i
        i += 1

def part_two(input_string: str) -> int:
    i = 0
    while True:
        hash_hex_string = hashlib.md5((input_string + str(i)).encode()).hexdigest()
        if hash_hex_string[:6] == "000000":
            return i
        i += 1

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as f:
        input_string = f.read()

    print(part_one(input_string))
    print(part_two(input_string))
