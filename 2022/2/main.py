import os

choice_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def part_one(turns: list[list[str]]):
    def score_for_round(opponent: str, us: str) -> int:
        score = 0
        us = choice_map[us]
        opponent = choice_map[opponent]
        # always add our choice
        score += us
        # draw?
        if opponent == us:
            score += 3
        # did we win? we always win if our choice is after theirs in order rock, paper, scissors
        elif 1 + (us - 2) % 3 == opponent:
            score += 6
        return score  
    total_score = 0
    for turn in turns:
        total_score += score_for_round(turn[0], turn[1])
    return total_score

def part_two(turns: list[list[str]]):
    # rock, paper, scissors
    total_score = 0
    for turn in turns:
        opponent = choice_map[turn[0]]
        us = choice_map[turn[1]]
        if us == 1:
            # we need to lose
            total_score += 1 + (opponent - 2) % 3
        elif us == 2:
            # we need to draw - choose same as them
            total_score += 3 + opponent
        elif us == 3:
            # we need to win the round - choice choice to right- 
            total_score += 6 + 1 + (opponent) % 3
    return total_score

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    with open("input.txt", "r") as f:
        input_string = f.read().strip()
    lines = input_string.split("\n")
    turns = [line.split() for line in lines]
    print(part_one(turns))
    print(part_two(turns))


