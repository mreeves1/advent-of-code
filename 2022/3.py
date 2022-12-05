import itertools
import sys
from pathlib import Path
from typing import Tuple

"""
https://adventofcode.com/2022/day/3
"""


def main() -> Tuple[int, int]:
    """Return priority sums of elf rucksacks"""
    debug = True
    score_total_part_1 = 0
    score_total_part_2 = 0
    file_name = Path(__file__).parent / "3.txt"  # each input differs by user

    # Part 1: Priority sum of duplicate item
    part1_priority_sum = 0
    with open(file_name) as fh:
        for line in fh:
            line = line.strip()
            mid = int(len(line)/2)
            items1 = list(line[0:mid:1])
            items2 = list(line[mid::])
            common_item = list(set(items1) & set(items2))[0]  # use set intersection since we assume only one item
            if debug:
                print(f"common item: {common_item}")
            part1_priority_sum += get_priority(common_item)
    print(f"Part 1: Sum of common item priorities = {part1_priority_sum}")

    # Part 2: Priority sum of duplicate item among every 3 lines
    with open(file_name) as fh:
        elf_count = 1
        elves = []
        part2_priority_sum = 0
        for line1, line2, line3 in itertools.zip_longest(fh, fh, fh):  # gets 3 lines at a time
            elf1_items, elf2_items, elf3_items = tuple(list(x.strip()) for x in (line1, line2, line3))
            common_item = list(set(elf1_items) & set(elf2_items) & set(elf3_items))[0]  # use sets to find common item
            if debug:
                print(f"common item: {common_item}")
            part2_priority_sum += get_priority(common_item)
    print(f"Part 2: Priority sum of duplicate item among every 3 lines = {part2_priority_sum}")

    return part1_priority_sum, part2_priority_sum


def get_priority(item: str) -> int:
    """
    returns a priority based on item
    a through z have priorities 1 through 26
    A through Z have priorities 27 through 52
    :param item: str
    :return: int
    """

    if 97 <= ord(item) <= 122:  # a to z should be 1 to 26
        return ord(item) - 96
    elif 65 <= ord(item) <= 90:  # A to Z should be 27 to 52
        return ord(item) - 38
    else:
        print(f"Unknown item: {item}. Expecting a to z or A to Z.")
        sys.exit(5)


if __name__ == '__main__':
    print(main())
else:
    print("This is meant to be run directly and never imported.")
    sys.exit(5)
