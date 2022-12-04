import sys
from pathlib import Path
from typing import Tuple


def main() -> Tuple[int, int]:  # why can't I use tuple(int, int) ?
    """Return a tuple of elf with most calories and calories hey have"""
    debug = False
    elves = {}
    file_name = Path(__file__).parent / "1.txt"  # each input differs by user
    with open(file_name) as fh:
        elf = 0
        current_calories = 0
        max_calories = 0
        max_elf = 0

        for line in fh:
            if line == "\n":
                if debug:
                    print(f"elf: {elf}, calories: {current_calories}")
                if current_calories > max_calories:
                    max_calories = current_calories
                    max_elf = elf + 1  # 0 index

                elves[elf] = current_calories  # dictionary of elf to calories for debugging
                elf = elf + 1
                current_calories = 0
            else:
                current_calories = current_calories + int(line)

    return max_elf, max_calories


if __name__ == '__main__':
    print(main())
else:
    print("This is meant to be run directly and never imported.")
    sys.exit(1)
