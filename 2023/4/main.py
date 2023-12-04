import re
import os

pattern = re.compile(r"Card\s+[0-9]+:(.*)\|(.*)")

def part_one(lines: list[str]) -> int:
    total_points = 0
    for line in lines:
        search = re.search(pattern, line)
        if search is not None:
            winning_number_count = 0
            winning_numbers = [int(num) for num in search.group(1).split()]
            our_numbers = [int(num) for num in search.group(2).split()]

            for number in winning_numbers:
                if number in our_numbers:
                    winning_number_count += 1

            if winning_number_count != 0:
                scratch_card_value = 2**(winning_number_count - 1)
                total_points += scratch_card_value
        else:
            print("Search found none... this is a bug!")
            return -1
    return total_points


def part_two(lines: list[str]) -> int:
    scratchcard_counter = {}

    for idx, line in enumerate(lines):
        if idx not in scratchcard_counter:
            scratchcard_counter[idx] = 1

        search = re.search(pattern, line)
        if search is not None:
            winning_numbers = [int(num) for num in search.group(1).split()]
            our_numbers = [int(num) for num in search.group(2).split()]

            winning_count = sum(our_number in winning_numbers for our_number in our_numbers)
    
            for n in range(idx + 1, idx + winning_count + 1):
                scratchcard_counter[n] = scratchcard_counter.get(n, 1) + scratchcard_counter[idx]

    return sum(scratchcard_counter.values())


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    print(part_one(lines))
    print(part_two(lines))
