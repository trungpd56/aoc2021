#!/bin/bash


# day variable has no leading 0 and must be between 1 and 25
day=${1##+(0)}
if ((day < 1 || day > 25)); then
    echo "Invalid day input: $1. Must be between 1 and 25."
    exit 1
fi
# project vartiable is "dayXX" where XX is the day variable
project=$(printf "day%02d" $1)

# get session cookie from file if .session exists
if [[ -f ".session" ]]; then
  AOC_SESSION=$(<".session")
fi

# validate session cookie
if [ -z "$AOC_SESSION" ]; then
    echo "AOC_SESSION isn't set. Cannot continue."
    exit 1
fi
VALIDSESSION=$(curl -s "https://adventofcode.com/2021/day/1/input" --cookie "session=${AOC_SESSION}")
if [[ $VALIDSESSION =~ "Puzzle inputs differ by user." ]] || [[ $VALIDSESSION =~ "500 Internal Server" ]]; then
    echo "Invalid AOC_SESSION. Cannot continue."
    exit 1
fi


if [[ -d "${project}" ]]; then
    cd $project
    exit 0
fi

mkdir ${project}

cd ${project}

curl -s "https://adventofcode.com/2021/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

# solution stub
cat > day${day}.py << EOF
#!/usr/bin/env python3

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""

def part1(data):
    """Solve part 1."""

def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent / "input.txt"
    puzzle_input = pathlib.Path(infile).read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    if solution1:
        print(f" part1: {solution1}")
    if solution2:
        print(f" part2: {solution2}")
EOF

# testing stub
cat > test_day${day}.py << EOF
import pathlib
import pytest
import day${day} as aoc

# PUZZLE_DIR = pathlib.Path(__file__).parent
#
# @pytest.fixture
# def example():
#    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
#    return puzzle_input

@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        ("", ""),
        ("", ""),
        ("", "")
    ])
def test_part1(puzzle_input, expected):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(puzzle_input)
    assert aoc.part1(parsed_input) == expected

@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        ("", ""),
        ("", ""),
        ("", "")
    ])
def test_part2(puzzle_input, expected):
    """Test part 2 on example input."""
    parsed_input = aoc.parse(puzzle_input)
    assert aoc.part2(parsed_input) == expected
EOF

