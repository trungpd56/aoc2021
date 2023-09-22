import pathlib
import pytest
import day13 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
   puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
   return puzzle_input

def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert (6, 10) in parsed_input[0]
    assert parsed_input[1][0] == 'fold along y=7'
    part1, part2 = aoc.solution(parsed_input)
    assert part1 == 17
    assert part2[:8] == "#####\n#."
